from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def library_root(request):
    return HttpResponse('''
    <a href="посилання на яке відправить користувача">Текст на який треба натиснути</a>
    <a href="/books/">Сторінка книг</a>
    <a href="/">Домашня сторінка</a>
    <a href="/orders/done/">Виконані замовлення</a>
''')
