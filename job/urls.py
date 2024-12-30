from django.urls import path
from .views import create,show,update,delete

urlpatterns = [
    path('create/', create, name='create'),
    path('show/', show, name='show'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
]