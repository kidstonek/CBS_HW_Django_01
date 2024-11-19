from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def orders_all(request):
    return HttpResponse('''
    <a href="/">Домашня сторінка</a></li>
    <a href="/orders/done/">Виконані замовлення</a>
    <a href="/orders/canceled/">Скасовані замовлення</a>
''')


def orders_done(request):
    return HttpResponse('''
    <h1>Done orders</h1>
''')


def orders_canceled(request):
    return HttpResponse('''
    <h1>Canceled orders</h1>
''')