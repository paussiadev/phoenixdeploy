from django.urls import path
from producao.views import ProducaoListView, ProducaoDetailView, ProducaoCreateView, ProducaoUpdateView, ProducaoDeleteView

urlpatterns = [
    path('', ProducaoListView.as_view(), name='producao_list'),
    path('create/', ProducaoDetailView.as_view(), name='producao_detail'),
    path('<int:pk>/', ProducaoCreateView.as_view(), name='producao_create'),
    path('<int:pk>/edit/', ProducaoUpdateView.as_view(), name='producao_update'),
    path('<int:pk>/delete/', ProducaoDeleteView.as_view(), name='producao_delete'),
]