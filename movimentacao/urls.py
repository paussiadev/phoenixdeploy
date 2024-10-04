from django.urls import path
from movimentacao.views import MovimentacaoListView, MovimentacaoDetailView, MovimentacaoCreateView, MovimentacaoUpdateView, MovimentacaoDeleteView

urlpatterns = [
    path('', MovimentacaoListView.as_view(), name='movimentacao_list'),
    path('create/', MovimentacaoDetailView.as_view(), name='movimentacao_create'),
    path('<int:pk>/', MovimentacaoCreateView.as_view(), name='movimentacao_detail'),
    path('<int:pk>/edit/', MovimentacaoUpdateView.as_view(), name='movimentacao_update'),
    path('<int:pk>/delete/', MovimentacaoDeleteView.as_view(), name='movimentacao_delete'),
]