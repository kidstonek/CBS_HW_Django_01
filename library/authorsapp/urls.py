from django.urls import path
from .views import *

urlpatterns = [
    path('', authors_all),
    path('top/', authors_top),
    path('ukraine/', authors_ukraine),
    path('usa/', authors_usa),
    path('top/ukraine/', authors_ukraine_top)
]