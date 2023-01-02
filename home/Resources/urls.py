from django.urls import path
from . import views

urlpatterns = [
    path('', views.ResourceList.as_view(), name='resource-list'),
    path('<int:pk>/', views.ResourceDetail.as_view(), name='resource-detail'),
]