from django.contrib.auth import authenticate,get_user_model
from django.shortcuts import render
from rest_framework import generics, status,viewsets,permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SignUpSerializer
from .tokens import create_jwt_pair_for_user

# Create your views here.


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = []

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {"message": "User Created Successfully", "data": serializer.data}

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = []
    authentication_classes=[]

    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")
        email = request.data.get("email")
        phone = request.data.get("phone")   
        
        if email:
            user = authenticate(email=email, password=password)
        elif phone:
            user = get_user_by_phone(phone, password)
        else:
            return Response(data={"message": "Please provide a username, email, or phone number"})

        if user is not None:

            tokens = create_jwt_pair_for_user(user)

            user_data = {
            'email': user.email,
            'username': user.username,
            'phone': user.phone,
            }

            response = {"message": "Login Successfull","user_data":user_data,"tokens": tokens}
            return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(data={"message": "Invalid email or password"},status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}

        return Response(data=content, status=status.HTTP_200_OK)

def get_user_by_phone(phone, password):
    try:
        user = get_user_model().objects.get(phone=phone)
        if user.check_password(password):
            return user
        else:
            return None
    except get_user_model().DoesNotExist:
        return None        

class ChangePasswordView(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def update(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not user.check_password(old_password):
            return Response({"error": "Old password is incorrect."}, status=status.HTTP_400_BAD_REQUEST)

        if not new_password:
            return Response({"error": "New password is required."}, status=status.HTTP_400_BAD_REQUEST)

        if len(new_password) < 8:
            return Response({"error": "New password must be at least 8 characters long."}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()
        return Response(status=status.HTTP_200_OK,message="you password have been updated")