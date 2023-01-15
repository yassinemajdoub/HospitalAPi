from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import ProviderSerializer
from .models import Provider
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from patients.permissions import IsProvider

class ProviderListView(generics.ListCreateAPIView):
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    permission_classes = [IsAuthenticated,IsProvider]

    filterset_fields = ['id', 'name', 'specialty', 'contact']
    search_fields = ['id', 'name', 'specialty', 'contact']
    ordering_fields = ['id', 'name', 'specialty', 'contact']

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class ProviderDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,IsProvider]
    
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

    def delete(self, request, *args, **kwargs):
        provider = get_object_or_404(Provider, pk=kwargs['pk'])
        provider.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)