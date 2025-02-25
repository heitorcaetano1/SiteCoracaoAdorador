from django.urls import path
from .views import ListaProdutoView, DetalheProdutoView

urlpatterns = [
    path('', ListaProdutoView.as_view(), name='produtos'),
    path('<int:pk>/', DetalheProdutoView.as_view(), name='produto'),
]