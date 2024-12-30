from django.urls import path
from .views import create,show,update

urlpatterns = [
    path('create/', create, name='create'),
    path('show/', show, name='show'),
    path('update/<int:id>/', update, name='update'),
]