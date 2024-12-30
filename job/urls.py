from django.urls import path
from .views import create,show

urlpatterns = [
    path('create/', create, name='create'),
    path('show/', show, name='show'),
]