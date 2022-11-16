from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('', include('pages.urls')),
    path('', include('books.urls')),
    
    path('login/', TemplateView.as_view(template_name="accounts/login.html"), name='login'),
    path('register/', TemplateView.as_view(template_name="accounts/register.html"), name='register'),

    # path('login/', TemplateView.as_view(template_name="accounts/login-v2.html"), name='login'),
    # path('register/', TemplateView.as_view(template_name="accounts/register-v2.html"), name='register'),

    # path('profile/', TemplateView.as_view(template_name="accounts/profile.html"), name='register'),
]
