from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import SignupView, MeView, DeleteView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('me/', MeView.as_view(), name='me'),
    path('delete/', DeleteView.as_view(), name='delete'),
]
