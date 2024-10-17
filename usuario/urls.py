from django.urls import path
from usuario.views import UserProfileView, UserProfileUpdateView

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/edit/', UserProfileUpdateView.as_view(), name='profile_edit'),
]