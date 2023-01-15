from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, status
from rest_framework.decorators import APIView, api_view, permission_classes
from rest_framework.permissions import (IsAuthenticated,AllowAny)
from rest_framework import filters
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Patient,LabResult,Appointment
from .serializers import PatientSerializer,LabResultSerializer,AppointmentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsProvider



# @api_view(http_method_names=["GET", "POST"])
# @permission_classes([AllowAny])
# def homepage(request: Request):

#     if request.method == "POST":
#         data = request.data

#         response = {"message": "Hello World", "data": data}

#         return Response(data=response, status=status.HTTP_201_CREATED)

#     response = {"message": "Hello World"}
#     return Response(data=response, status=status.HTTP_200_OK)




class PatientListCreateView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):

    """
    a view for creating and listing posts
    """

    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated,IsProvider]
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]

    filterset_fields = ['id','full_name','address','email','phone','emergency_contact_phone']
    search_fields = ['id','full_name','address','email','phone','emergency_contact_phone']
    ordering_fields = ['id','full_name','address','email','phone','emergency_contact_phone']


    queryset = Patient.objects.all()

    def perform_create(self, serializer):
        serializer.save()
        return super().perform_create(serializer)

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PatientRetrieveUpdateDeleteView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    permission_classes = [IsAuthenticated,IsProvider]
    
    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class LabResultCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,IsProvider]

    queryset = LabResult.objects.all()
    serializer_class = LabResultSerializer        

class LabResultList(generics.ListAPIView):
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]

    filterset_fields = ['id', 'patient', 'test_name','test_date','test_result']
    search_fields = ['id', 'patient', 'test_name','test_date','test_result']
    ordering_fields = ['id', 'patient', 'test_name','test_date','test_result']

    permission_classes = [IsAuthenticated]
    queryset = LabResult.objects.all()
    serializer_class = LabResultSerializer


from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from .serializers import AppointmentSerializer

class AppointmentListView(generics.ListCreateAPIView):
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]

    filterset_fields = ['id', 'patient', 'provider', 'date_time', 'location', 'reason', 'notes']
    search_fields = ['id', 'patient', 'provider', 'date_time', 'location', 'reason', 'notes']
    ordering_fields = ['id', 'patient', 'provider', 'date_time', 'location', 'reason', 'notes']

    serializer_class = AppointmentSerializer

    def get_queryset(self):
        return Appointment.objects.filter(patient=self.kwargs['patient_id'])

class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_object(self, **kwargs):
        return get_object_or_404(Appointment, patient=self.kwargs['patient_id'],
         pk=self.kwargs['pk'])

    def delete(self, request, *args, **kwargs):
        appointment = get_object_or_404(Appointment, patient=kwargs['patient_id'],
         pk=kwargs['pk'])
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)