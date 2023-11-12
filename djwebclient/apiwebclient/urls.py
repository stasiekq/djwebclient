from django.urls import path
from .views import index, create_update, get, delete, get_all

urlpatterns = [
    path('', index, name='index'),
    path('create-update/', create_update, name='create_update'),
    path('get/', get, name='get'),
    path('delete/', delete, name='delete'),
    path('get-all/', get_all, name='get_all'),
]