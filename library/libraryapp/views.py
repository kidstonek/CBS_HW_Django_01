from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def library_root(request):
    return HttpResponse('''
    <a href="/">Домашня сторінка</a></li>
    <a href="/authors/">Сторінка авторів</a>
    <a href="/books/">Сторінка книг</a>
    <a href="/orders/done/">Виконані замовлення</a>
''')
