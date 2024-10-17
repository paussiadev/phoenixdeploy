from django.urls import path
from material.views import MaterialListView, MaterialDetailView, MaterialCreateView, MaterialUpdateView, MaterialDeleteView

urlpatterns = [
    path('', MaterialListView.as_view(), name='material_list'),
    path('create/', MaterialCreateView.as_view(), name='material_create'),
    path('<int:pk>/', MaterialDetailView.as_view(), name='material_detail'),
    path('<int:pk>/edit/', MaterialUpdateView.as_view(), name='material_update'),
    path('<int:pk>/delete/', MaterialDeleteView.as_view(), name='material_delete'),
]