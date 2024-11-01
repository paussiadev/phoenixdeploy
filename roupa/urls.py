from django.urls import path
from roupa.views import RoupaListView, RoupaDetailView, RoupaCreateView, RoupaUpdateView, RoupaDeleteView

urlpatterns = [
    path('', RoupaListView.as_view(), name='roupa_list'),
    path('<int:pk>/', RoupaDetailView.as_view(), name='roupa_detail'),
    path('create/', RoupaCreateView.as_view(), name='roupa_create'),
    path('<int:pk>/edit/', RoupaUpdateView.as_view(), name='roupa_update'),
    path('<int:pk>/delete/', RoupaDeleteView.as_view(), name='roupa_delete'),
]