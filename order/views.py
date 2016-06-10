import json
import urllib
from django.conf import settings

from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from paypal.pro.helpers import PayPalWPP
from order.order_lib import get_cart_data_from_request, create_order_from_paypal_for_review, create_order_from_express_paypal, create_order_from_direct_paypal, send_order_email


def paypal_start(request):
    """
    Creating express checkout request from users cart
    """
    try:
        params = get_cart_data_from_request(request)
        host_name = request.get_host()

        params.update({
            "returnurl": "http://" + host_name + "/order/paypal/confirm",
            "cancelurl": "http://" + host_name + "/#!/cart",
            "noshipping": 2,
        })

        wpp = PayPalWPP()
        nvp = wpp.setExpressCheckout(params)

        response = HttpResponseRedirect(settings.PAYPAL_URL + '/cgi-bin/webscr?cmd=_express-checkout&token=' + nvp.token)
        response.delete_cookie('cart')
        return response
    except Exception, e:
        #log error here
        print e
        return HttpResponseRedirect("/#!/cart")


def paypal_confirm(request):
    """
    Return from Paypal and create confirmation page
    """
    wpp = PayPalWPP(request)

    token = request.GET.get("token", "")

    params = {"token": token}
    nvp = wpp.getExpressCheckoutDetails(params)

    """
    <QueryDict: {
        u'l_paymentrequest_0_number1': [u'7'],
        u'l_paymentrequest_0_number0': [u'6'],
        u'shippingamt': [u'0.00'],
        u'paymentrequest_0_shiptozip': [u'123456'],
        u'paymentrequest_0_shiptostreet': [u'Pug str, 15'],
        u'paymentrequest_0_shiptocountryname': [u'Russia'],
        u'l_paymentrequest_0_taxamt1': [u'0.00'],
        u'paymentrequest_0_shiptoname': [u'Second'],
        u'shiptocountryname': [u'Russia'],
        u'paymentrequestinfo_0_errorcode': [u'0'],
        u'l_paymentrequest_0_taxamt0': [u'0.00'],
        u'l_paymentrequest_0_amt1': [u'26.00'],
        u'l_paymentrequest_0_amt0': [u'29.00'],
        u'checkoutstatus': [u'PaymentActionNotInitiated'],
        u'billingagreementacceptedstatus': [u'0'],
        u'l_paymentrequest_0_name1': [u'Casual summer dress'],
        u'l_paymentrequest_0_name0': [u'Vintage faux fur vest'],
        u'l_taxamt0': [u'0.00'],
        u'shipdiscamt': [u'0.00'],
        u'paymentrequest_0_shipdiscamt': [u'0.00'],
        u'paymentrequest_0_addressstatus': [u'Unconfirmed'],
        u'lastname': [u'buyer'],
        u'paymentrequest_0_shiptocity': [u'Moscow'],
        u'correlationid': [u'ed7766d969878'],
        u'addressstatus': [u'Unconfirmed'],
        u'email': [u'fr_joy-buyer@mail.ru'],
        u'build': [u'16751317'],
        u'l_paymentrequest_0_qty1': [u'1'],
        u'l_paymentrequest_0_qty0': [u'1'],
        u'payerstatus': [u'verified'],
        u'paymentrequest_0_insuranceamt': [u'0.00'],
        u'firstname': [u'test'],
        u'paymentrequest_0_currencycode': [u'USD'],
        u'timestamp': [u'2015-05-22T15:34:54Z'],
        u'currencycode': [u'USD'],
        u'paymentrequest_0_amt': [u'55.00'],
        u'paymentrequest_0_handlingamt': [u'0.00'],
        u'insuranceamt': [u'0.00'],
        u'handlingamt': [u'0.00'],
        u'paymentrequest_0_insuranceoptionoffered': [u'false'],
        u'l_taxamt1': [u'0.00'], u'amt': [u'55.00'],
        u'paymentrequest_0_itemamt': [u'55.00'],
        u'paymentrequest_0_shiptocountrycode': [u'RU'],
        u'payerid': [u'3PMMXLXMPWBRC'],
        u'ack': [u'Success'],
        u'taxamt': [u'0.00'],
        u'token': [u'EC-915576968K751545E'],
        u'paymentrequest_0_taxamt': [u'0.00'],
        u'itemamt': [u'55.00'],
        u'paymentrequest_0_shippingamt': [u'0.00'],
    """

    order = create_order_from_paypal_for_review(nvp)

    response = HttpResponseRedirect("/#!/order/confirm")
    response.set_cookie("order_type", "express")
    response.set_cookie("order", json.dumps(order))
    return response


def paypal_end(request):
    """
    Do payment and create order object in DB
    """
    try:
        wpp = PayPalWPP(request)
        token = request.GET['token']
        params = {"token": token}
        nvp = wpp.getExpressCheckoutDetails(params)
        order_dict = nvp.response_dict.copy()

        params = {
            "token": token,
            "payerid": nvp.payerid,
            "paymentrequest_0_amt": nvp.response_dict.get("paymentrequest_0_amt"),
            "paymentrequest_0_currencycode" : nvp.response_dict.get("paymentrequest_0_currencycode")
        }

        payment = wpp.doExpressCheckoutPayment(params)

        order_dict['transactionid'] = payment.response_dict.get('paymentinfo_0_transactionid')

        order = create_order_from_express_paypal(order_dict)
        send_order_email(order.email, order, order.items.all)

        data = {
            'order_id': order.id,
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    except Exception, e:

        print e
        data = {
            'error': e.message
        }
        return HttpResponseServerError(json.dumps(data), content_type='application/json')


def save(request):
    """
    Direct Paypal payment with credit card
    """
    try:
        cart = get_cart_data_from_request(request)

        if 'order' not in request.GET:
            raise Exception('no order data')

        order_json = request.GET['order']
        order_json = urllib.unquote(order_json)
        order = json.loads(order_json)

        wpp = PayPalWPP()

        paypal_params = {
            'ipaddress': request.META.get('REMOTE_ADDR'),
            'creditcardtype': order['creditcardtype'],
            'acct': order['acct'],
            'expdate': order['cardmonth'] + order['cardyear'],
            'cvv2': order['cvv2'],
            'email': order['email'],
            'firstname': order['card_first_name'],
            'lastname': order['card_last_name'],

            'street': order['b_street'],
            'city': order['b_city'],
            'state': order['b_state'],
            'countrycode': order['b_countrycode'],
            'zip': order['b_zip'],

            'amt': cart['paymentrequest_0_amt'],
        }

        nvp = wpp.doDirectPayment(paypal_params)

        order_data = nvp.response_dict.copy()
        order_data.update(cart)
        order_data.update(order)


        order = create_order_from_direct_paypal(order_data)

        data = {
            'order_id': order.id,
        }

        send_order_email(order.email, order, order.items.all)
        return HttpResponse(json.dumps(data), content_type='application/json')

    except Exception, e:
        print e

        data = {
            'error': e.message
        }
        return HttpResponseServerError(json.dumps(data), content_type='application/json')