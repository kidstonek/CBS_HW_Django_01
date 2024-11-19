from django.urls import path
from .views import *

urlpatterns = [
    path('', books_all),
    path('top/', books_top),
    path('free/', books_free),
    path('top/free/', books_top_free),
    path('oldschool/', books_oldschool)
]