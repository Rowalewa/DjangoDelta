from django.http import HttpResponse
from django.shortcuts import render
from django_daraja.mpesa.core import MpesaClient


def index(request):
    cl = MpesaClient()
    phone_number = '0791589514'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'description'
    callback_url = 'https://darajambili.herokuapp.com/express_payment'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)


def stk_push_callback(request):
    data = request.body
    return HttpResponse('stk push in Django')
