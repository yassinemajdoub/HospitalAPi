from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Resource
from .serializers import ResourceSerializer
from rest_framework.permissions import IsAuthenticated
from patients.permissions import IsProvider

class ResourceList(generics.ListCreateAPIView):
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    permission_classes = [IsAuthenticated,IsProvider]

    filterset_fields = ['id', 'name', 'type', 'availability']
    search_fields = ['id', 'name', 'type', 'availability']
    ordering_fields = ['id', 'name', 'type', 'availability']

    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

    def perform_create(self, serializer):
        serializer.save()
        return super().perform_create(serializer)

class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,IsProvider]
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
