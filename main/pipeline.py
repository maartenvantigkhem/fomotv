"""
Hooks for saving additional info about users from social networks (Facebook, Instagram)
"""
from django.core.files.base import ContentFile
from requests import request, ConnectionError
from social.apps.django_app.default.models import UserSocialAuth

import mailchimp
#Mailchimp APIs.
#TODO: This needs to be relocated to somewhere else. Not sure where, though.
API_KEY = 'd7288688f44cb7608ba5556680625a4a-us12'
LIST_ID = 'db4a429107'


def save_profile(backend, user, response, *args, **kwargs):
    """
    get and save avatars from fb and instagram
    """
    avatar = user.avatar
    if (not avatar or avatar == '') and backend.name in ['facebook', 'instagram']:
        if backend.name == 'facebook':
            url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
        if backend.name == "instagram":
            url = response['data']['profile_picture']

        try:
            file_response = request('GET', url, params={'type': 'large'})
            file_response.raise_for_status()

            user.avatar.save('{0}.jpg'.format(user.id),
                             ContentFile(file_response.content),
                             save=False
                             )
            user.save()
        except ConnectionError as e:
            print e
            pass
        except Exception as e:
            print e
            pass
 
#Author - Vik.
#Date: 28-Nov-2015
#Description: Add a plug into the Social Auth Pipeline to add a user to mailchimp.
def add_user_to_mailchimp(backend, user, response, *args, **kwargs):
    
        #Let's do a quick check to see whether they are present in the mailchimp list.
        #If not, add them.
    try:
        _username = response['name']
        email = user.email
        api = mailchimp.Mailchimp(API_KEY)
        api.lists.subscribe(LIST_ID, {
            'email': email
            }, {
            'FNAME': _username
        }, 'html', {
            'double_optin':'false'
        })
    except:
        print ("User already exists in MailChimp")
    