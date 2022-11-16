from django.urls import path

from books.views import PublisherListView

urlpatterns = [
    path('publishers/', PublisherListView.as_view()),
    # path('register/', register_user, name="register"),
    # path("logout/", LogoutView.as_view(), name="logout")
]