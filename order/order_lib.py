import json
import re
import urllib
from django.conf import settings
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
from main.models import Prize
from order.models import Order, OrderItem


def set_size_and_color_to_paypal(item):
    ret = ""
    if item['_data'].get('size') is not None:
        ret += "Size: "+ item['_data'].get('size')

    if item['_data'].get('color') is not None:
        if ret != "":
            ret += ", "
        ret += "Color: "+ item['_data'].get('color')
    return ret


def get_size_and_color_from_paypal(desc):
    if desc is None:
        return None, None
    ret = re.split(':|,',desc)
    if len(ret) == 4:
        return ret[1].strip(), ret[3].strip()
    return None, None


def get_cart_data_from_request(request):
    if 'cart' not in request.COOKIES:
        raise Exception('no cart data')

    try:
        cart_json = request.COOKIES['cart']
        cart_json = urllib.unquote(cart_json)
        cart = json.loads(cart_json)

        if 'items' not in cart or len(cart['items']) == 0:
            raise Exception('cart is empty')


        """
        {
        "shipping":null,
        "taxRate":null,
        "tax":null,
        "items":[{
            "_id":6,
            "_name":"Vintage faux fur vest",
            "_price":29,
            "_quantity":1,
            "_data":
                {"image":"http://localhost:8000/media/product_photo/il_570xN.544796314_i9ue.jpg","competition_id":4}
            },
            {"_id":7,
            "_name":"Casual summer dress",
            "_price":26,
            "_quantity":1,
            "_data":{"image":"http://localhost:8000/media/product_photo/vintage_beach_dress.jpg",
        "competition_id":4}}]}
        """

        params = dict()

        total_cost = 0.0
        total_shipping = cart['shipping']
        for index, item in enumerate(cart['items']):
            index = str(index)
            params['l_paymentrequest_0_name' + index] = item['_name']
            params['l_paymentrequest_0_amt' + index] = item['_price']
            params['l_paymentrequest_0_number' + index] = item['_id']
            params['l_paymentrequest_0_qty' + index] = item['_quantity']

            params['l_paymentrequest_0_desc' + index] = set_size_and_color_to_paypal(item)

            total_cost += float(item['_price'])*int(item['_quantity'])

        params['paymentrequest_0_itemamt'] = round(total_cost,2)
        params['paymentrequest_0_shippingamt'] = total_shipping
        params['paymentrequest_0_amt'] = round(total_cost,2) + total_shipping
        params['paymentrequest_0_currencycode'] = "AUD"

        return params
    except Exception, e:
        raise e


#atom trans action needed!
def create_order_from_direct_paypal(nvp_dict):
    """
    Create order in DB with ordered items
    """
    #create order
    #create items
    #return order object
    """
    <QueryDict:
    {u'l_paymentrequest_0_number0': [4],
     u's_countrycode': [u'AX'],
     u'b_state': [u'sdf'],
     u'card_first_name': [u'sdf'],
     u's_last_name': [u'sdf'],
     u's_street': [u'sdf'],
     u'acct': [u'4239530610456015'],
     u'l_paymentrequest_0_amt0': [32],
     u'l_paymentrequest_0_name0': [u'Raw Edge Design Letters Print Black Polyester VEST'],
     u's_city': [u'sdf'],
     u's_state': [u'sdf'],
     u'version': [u'116.0'],
     u's_countryname': [u'Aland Islands'],
     u'build': [u'16770825'],
     u'cvv2': [u'123'],
     u'b_street': [u'dd'],
     u'email': [u'fr_joy@mail.ru'],
     u'l_paymentrequest_0_qty0': [2],
     u'b_countrycode': [u'AU'],
     u'b_countryname': [u'Afghanistan'],
     u'timestamp': [u'2015-06-14T10:22:07Z'],
     u'currencycode': [u'USD'],
     u'card_last_name': [u'sdf'],
     u's_zip': [u'dsf'],
     u'paymentrequest_0_amt': [64.0],
     u'phone': [u'sdf'],
     u'b_country': [u'1'],
     u'cardyear': [u'2020'],
     u'transactionid': [u'06M899763J781091D'],
     u'amt': [u'64.00'],
     u's_first_name': [u'sdf'],
     u'cvv2match': [u'M'],
     u'cardmonth': [u'05'],
     u'ack': [u'Success'],
     u'b_city': [u'sdf'],
     u'creditcardtype': [u'visa'],
     u'b_last_name': [u'dddddd'],
     u'b_zip': [u'sdf'],
     u'avscode': [u'X'],
     u'b_first_name': [u'sads'],
     u'correlationid': [u'dba9b733e476']}>
    """

    order = Order()
    order.email = nvp_dict.get('email')
    order.phone = nvp_dict.get('phone', "")

    order.b_first_name = nvp_dict.get('b_first_name')
    order.b_last_name = nvp_dict.get('b_last_name')
    order.b_address_countryname = nvp_dict.get('b_countryname')
    order.b_address_countrycode = nvp_dict.get('b_countrycode')
    order.b_address_zip = nvp_dict.get('b_zip')
    order.b_address_state = nvp_dict.get('b_state')
    order.b_address_city = nvp_dict.get('b_city')
    order.b_address_street = nvp_dict.get('b_street')

    order.status = order.NEW_ORDER
    order.paypal_transaction_id = nvp_dict.get('transactionid')
    order.save()

    save_order_items(nvp_dict, order)

    return order


def create_order_from_express_paypal(nvp_dict):
    """
    Create order in DB with ordered items
    """
    #create order
    #create items
    #return order object

    order = Order()
    order.email = nvp_dict.get('email')
    order.b_first_name = nvp_dict.get('firstname')
    order.b_last_name = nvp_dict.get('lastname')

    order.b_address_countryname = nvp_dict.get('shiptocountryname')
    order.b_address_countrycode = nvp_dict.get('shiptocountrycode')
    order.b_address_zip = nvp_dict.get('shiptozip')
    order.b_address_state = nvp_dict.get('shiptostate')
    order.b_address_city = nvp_dict.get('shiptocity')
    order.b_address_street = nvp_dict.get('shiptostreet') \
                        + nvp_dict.get('shiptostreet2', "")

    order.status = order.NEW_ORDER
    order.paypal_transaction_id = nvp_dict.get('transactionid')
    order.save()

    save_order_items(nvp_dict, order)

    return order


def save_order_items(nvp_dict, order):
    item_ids = [(key, value) for key, value in nvp_dict.iteritems() if key.startswith("l_paymentrequest_0_number")]

    print item_ids

    for index, i in enumerate(item_ids):
        product = Prize.objects.get(pk=i[1])

        order_item = OrderItem()
        order_item.order_id = order.id
        order_item.product = product
        order_item.number = product.number
        order_item.name = product.name
        order_item.amount = nvp_dict.get('l_paymentrequest_0_amt' + str(index))
        order_item.quantity = nvp_dict.get('l_paymentrequest_0_qty' + str(index))

        order_item.size, order_item.color \
            = get_size_and_color_from_paypal(nvp_dict.get('l_paymentrequest_0_desc' + str(index)))

        print nvp_dict.get('l_paymentrequest_0_desc' + str(index))

        order_item.save()


def create_order_from_paypal_for_review(nvp):
    """
    From Paypal NVP to plain python dict for review page
    """
    order = dict()
    order['email'] = nvp.response_dict['email']
    order['token'] = nvp.response_dict['token']
    order['b_first_name'] = nvp.response_dict['firstname']
    order['b_last_name'] = nvp.response_dict['lastname']

    order['b_countryname'] = nvp.response_dict.get('paymentrequest_0_shiptocountryname')
    order['b_countrycode'] = nvp.response_dict.get('paymentrequest_0_shiptocountrycode')
    order['b_zip'] = nvp.response_dict.get('paymentrequest_0_shiptozip')
    order['b_city'] = nvp.response_dict.get('paymentrequest_0_shiptocity')
    order['b_street'] = nvp.response_dict.get('paymentrequest_0_shiptostreet')
    order['b_street2'] = nvp.response_dict.get('paymentrequest_0_shiptostreet2',"")
    order['b_state'] = nvp.response_dict.get('paymentrequest_0_shiptostate',"")

    return order


def send_order_email(email, order, products):
    subject, from_email, to_email = u'Your order in Prized.tv', \
                                    'products@prized.tv', \
                                    (email, )

    html_data = get_template('email/new_order.html')

    d = Context({
        'order_id': order.id,
        'order': order,
        'products': products,
    })

    #DEBUG NOTE: If you see an error 61 (connection refused) being thrown by the server
    #after the call to msg.send(), it means that your EMAIL_BACKEND is not correctly
    #defined in settings.py
    
    #Send email to client
    html_content = html_data.render(d)
    msg = EmailMessage(subject, html_content, from_email, to_email)
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()

    #Send email to site manager
    msg = EmailMessage(subject, html_content, from_email, to=['vikram@f2pictures.com'])
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()

