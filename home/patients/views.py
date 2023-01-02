from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, status
from rest_framework.decorators import APIView, api_view, permission_classes
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)
from rest_framework import filters
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Patient,LabResult,Appointment
from .serializers import PatientSerializer,LabResultSerializer,AppointmentSerializer
from django_filters.rest_framework import DjangoFilterBackend
# from .permissions import ReadOnly, AuthorOrReadOnly
from rest_framework.pagination import PageNumberPagination


# class CustomPaginator(PageNumberPagination):
#     page_size = 3
#     page_query_param = "page"
#     page_size_query_param = "page_size"


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def homepage(request: Request):

    if request.method == "POST":
        data = request.data

        response = {"message": "Hello World", "data": data}

        return Response(data=response, status=status.HTTP_201_CREATED)

    response = {"message": "Hello World"}
    return Response(data=response, status=status.HTTP_200_OK)




class PatientListCreateView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):

    """
    a view for creating and listing posts
    """

    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]

    filterset_fields = ['id','full_name','address','email','phone','emergency_contact_phone']
    search_fields = ['id','full_name','address','email','phone','emergency_contact_phone']
    ordering_fields = ['id','full_name','address','email','phone','emergency_contact_phone']

    # pagination_class = CustomPaginator
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
    permission_classes = [IsAuthenticated]
    
    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class LabResultCreate(generics.CreateAPIView):
    permission_classes = []

    queryset = LabResult.objects.all()
    serializer_class = LabResultSerializer        

class LabResultList(generics.ListAPIView):
    queryset = LabResult.objects.all()
    serializer_class = LabResultSerializer


from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from .serializers import AppointmentSerializer

class AppointmentListView(generics.ListCreateAPIView):
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



# @api_view(http_method_names=["GET"])
# # @permission_classes([IsAuthenticated])
# @permission_classes([])
# def get_posts_for_current_user(request: Request):
#     user = request.user

#     serializer = CurrentUserPostsSerializer(instance=user, context={"request": request})

#     return Response(data=serializer.data, status=status.HTTP_200_OK)


# class ListPostsForAuthor(generics.GenericAPIView, mixins.ListModelMixin):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer
#     permission_classes = []
#     # permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         username = self.request.query_params.get("username") or None

#         queryset = Patient.objects.all()

#         if username is not None:
#             return Patient.objects.filter(author__username=username)

#         return queryset

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
