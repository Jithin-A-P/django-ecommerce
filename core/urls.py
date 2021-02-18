from core.views import item_list
from django.urls import path
from django.urls import path
from .views import item_list

app_name = 'core'

urlpatterns = [
    path('', item_list, name='item-list'),
]
