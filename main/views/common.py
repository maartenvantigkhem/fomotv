import urllib2

from PIL import Image, ImageOps

from django.core.files.base import ContentFile
from django.core.urlresolvers import reverse
from django.shortcuts import render
import json

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth import login
from paypal.standard.forms import PayPalPaymentsForm
from requests import ConnectionError
from social.apps.django_app.default.models import UserSocialAuth

from social.backends.oauth import BaseOAuth1, BaseOAuth2
from social.apps.django_app.utils import psa
from main.models import Competition, Photo, Config
from order.models import Order
from order.order_lib import send_order_email


def get_user_profile_params(request):
    params = dict()

    params['facebook_app_id'] = settings.SOCIAL_AUTH_FACEBOOK_KEY
    params['instagram_app_id'] = settings.SOCIAL_AUTH_INSTAGRAM_KEY
    params['social_auth_type'] = ""
    params['social_user_id'] = ""

    if request.user.is_authenticated():
        res = UserSocialAuth.objects.filter(user_id=request.user.id)
        if res.count() > 0:
            params['social_auth_type'] = res[0].provider
            params['social_user_id'] = res[0].uid
        if request.user.avatar != '':
            params['avatar'] = request.user.avatar.url
            print request.user.avatar.url
        else:
            params['avatar'] = settings.DEFAULT_USER_AVATAR

    return params


def index(request):
    """
    Renders basic application layout
    """
    params = get_user_profile_params(request)

    competition = Competition.get_active()
    params['top_competition_id'] = competition.id
    params['minify_js'] = settings.MINIFY_JS

    params['first_page_text'] = ''
    config = Config.objects.all()
    if config.count() > 0:
        params['first_page_text'] = config[0].first_page_text

    #order email test
    #order = Order.objects.get(pk=25)
    #send_order_email(order.email, order, order.items.all)

    return render(request, 'base.html', params)


#This method is called from the auth-service.js file's login method.
#An access token is received and then the pipeline is invoked. The pipeline is invoked at the request.backend.do_auth line.
#Once the pipeline is complete, we return here and then do a login.
# Lastly, we populate the data that the front end needs and return it to them.
# https://github.com/omab/python-social-auth/blob/master/docs/pipeline.rst
@psa('social:complete')
def ajax_auth(request, backend):
    
    if isinstance(request.backend, BaseOAuth1):
        token = {
            'oauth_token': request.GET.get('access_token'),
            'oauth_token_secret': request.GET.get('access_token_secret'),
        }
    elif isinstance(request.backend, BaseOAuth2):
        token = request.GET.get('access_token')
    else:
        return HttpResponseBadRequest('Wrong backend type')
    
    #Invoke the python-social-auth pipeline
    user = request.backend.do_auth(token, ajax=True)
    
    #Perform the actual login - This is provided by the SocialAuth backends.
    login(request, user)

    #Get the avatar to prepare for return to front end. (Check pipeline.py for details)
    avatar = user.avatar.url if user.avatar and user.avatar != '' else settings.DEFAULT_USER_AVATAR

    #Prepare the data to be returned.
    data = {'id': user.id, 'username': user.username, 'terms_flag': user.terms_flag, 'avatar': avatar}

    res = UserSocialAuth.objects.filter(user_id=user.id)
    if res.count() > 0:
        data['social_user_id'] = res[0].uid
    return HttpResponse(json.dumps(data), content_type='application/json')


def resize_image(image_path):
    """
    resize user image with PIL
    """
    image = Image.open(image_path)

    imagefit = ImageOps.fit(image, (612, 612), Image.ANTIALIAS)
    imagefit.save(image_path, 'JPEG', quality=100)


def upload_photo_by_url(request):
    if not request.user.is_authenticated():
        return HttpResponseBadRequest('Auth needed')

    photo_url = request.POST.get('photo_url', None)

    if photo_url is None:
        return HttpResponseBadRequest('No photo')

    try:
        file_content = urllib2.urlopen(photo_url).read()
    except ConnectionError:
        return HttpResponseBadRequest('Connection error')

    competition_id = request.POST.get('competition_id', None)

    if not competition_id:
        return HttpResponseBadRequest('No competition')

    competition = Competition.objects.get(pk=competition_id)

    try:
        photo = Photo()
        photo.author = request.user
        photo.competition = competition
        photo.image.save(Photo.get_photo_name(),
                         ContentFile(file_content),
                         save=False
                         )
        photo.save()

        local_path = photo.image.name
        full_path = settings.MEDIA_ROOT + local_path
        #resize_image(full_path)
    except Exception:
        return HttpResponseBadRequest('Error while photo upload')
    except IOError:
        return HttpResponseBadRequest('Bad file format')

    data = {
        'photo_id': photo.id,
        'competition_id': photo.competition.id
    }
    return HttpResponse(json.dumps(data), content_type='application/json')


def upload_photo_from_file(request):

    if not request.user.is_authenticated():
        return HttpResponseBadRequest('Auth needed')

    if 'file' not in request.FILES:
        return HttpResponseBadRequest('No photo')

    data = request.FILES['file'] # or self.files['image'] in your form

    try:
        photo = Photo()
        photo.author = request.user
        photo.competition = Competition.get_active()
        photo.image.save(Photo.get_photo_name(),
                         ContentFile(data.read()),
                         save=False
                         )
        photo.save()

        local_path = photo.image.name
        full_path = settings.MEDIA_ROOT + local_path

        #resize_image(full_path)
    except IOError:
        return HttpResponseBadRequest('Bad file format')
    except Exception:
        return HttpResponseBadRequest('Error while photo upload')

    data = {
        'photo_id': photo.id,
        'competition_id': photo.competition.id
    }
    return HttpResponse(json.dumps(data), content_type='application/json')


def upload_photo_from_src(request):
    """
    Receive and save user photo from crop tool on front end
    Photo has 612*612 size
    """
    if not request.user.is_authenticated():
        return HttpResponseBadRequest('Auth needed')

    if 'imgsrc' not in request.POST:
        return HttpResponseBadRequest('No photo')

    data = request.POST['imgsrc'].split(',')[1].decode('base64') # or self.files['image'] in your form

    competition_id = request.POST.get('competition_id', None)

    if not competition_id:
        return HttpResponseBadRequest('No competition')

    competition = Competition.objects.get(pk=competition_id)

    photo = Photo()
    photo.author = request.user
    photo.competition = competition
    photo.image.save(Photo.get_photo_name(),
                     ContentFile(data),
                     save=False
                     )
    photo.save()

    data = {
        'photo_id': photo.id,
        'competition_id': photo.competition.id
    }
    return HttpResponse(json.dumps(data), content_type='application/json')

