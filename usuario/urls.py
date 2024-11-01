from django.urls import path
from usuario.views import UserPasswordChangeView, UserProfileView, UserProfileUpdateView

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/edit/', UserProfileUpdateView.as_view(), name='profile_edit'),
    path('profile/password/', UserPasswordChangeView.as_view(), name='password_change'),
]