from django.urls import path
from .views import *

urlpatterns = [
    path('', orders_all),
    path('done/', orders_done),
    path('canceled/', orders_canceled),
]