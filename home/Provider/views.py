from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import ProviderSerializer
from .models import Provider

class ProviderListView(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class ProviderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

    def delete(self, request, *args, **kwargs):
        provider = get_object_or_404(Provider, pk=kwargs['pk'])
        provider.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)