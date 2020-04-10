from django.urls import path
from .views import AccountView, LoginView

urlpatterns = [
    path('sign_up',AccountView.as_view()),
    path('sign_in',LoginView.as_view())
]
