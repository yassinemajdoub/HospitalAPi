from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProviderListView.as_view(), name='resource-list'),
    path('<int:pk>/', views.ProviderDetailView.as_view(), name='resource-detail'),
]