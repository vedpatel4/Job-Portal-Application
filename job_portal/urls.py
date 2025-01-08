from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('secret-admin-url/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', include('users.urls')),
    path('company/', include('company.urls')),
    path('job/', include('job.urls')),
]
