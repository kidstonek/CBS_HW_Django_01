from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def books_all(request):
    return HttpResponse('''
    <a href="/">Домашня сторінка</a>
    <a href="/books/top/">Список топових книг</a>
    <a href="/books/free/">Список безкоштовних книг</a>
    <a href="/books/top/free/">Список найкращих безкоштовних книг</a>
    <a href="/books/oldschool/">Список класичних книг</a>
''')


def books_top(request):
    return HttpResponse('''
    <h1>Top books</h1>
''')


def books_free(request):
    return HttpResponse('''
    <h1>Free books</h1>
''')


def books_top_free(request):
    return HttpResponse('''
    <h1>TOP Free books</h1>
''')


def books_oldschool(request):
    return HttpResponse('''
    <h1>Oldschool books</h1>
''')