from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import UserView

urlpatterns = [
    path('sign-in/', TokenObtainPairView.as_view()),
    path('sign-up/', UserView.as_view()),
]
