from django.urls import path
from dashboard.views import CustomLoginView, CustomLogoutView, HomePage


urlpatterns = [
    path('', HomePage.as_view(), name='dashboard'),
    path('login/', CustomLoginView.as_view(), name='login'), 
    path('logout/', CustomLogoutView.as_view(), name='logout'), 
]