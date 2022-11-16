from django.urls import path

from pages.views import GreetingView

urlpatterns = [
    path('about/', GreetingView.as_view()),
]