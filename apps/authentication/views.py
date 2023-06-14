from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.db import transaction
from apps.authentication.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

class RegisterUser(APIView):
    serializer_class = UserSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get("email")
            if User.objects.filter(email=email).exists():
                return Response(
                    {
                        "message": "Email already registered",
                        "code": "email_already_registered",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            with transaction.atomic():
                serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DetailsUser(APIView):
    permission_classes = [ IsAuthenticated ]
    serializer_class = UserSerializer

    def get(self, request):
        get_data = User.objects.get(pk=request.user.pk)
        user_serializer = UserSerializer(get_data).data
        data = {
            'user':user_serializer
        }
        return Response(data)
    
    def post(self, request):
        current_user = User.objects.get(pk=request.user.pk)
        email = request.data.get('email')
        password = request.data.get('password')
        current_user.username = email
        current_user.set_password(password)
        current_user.save()
        return Response({"message": "User update successfully"}, status=status.HTTP_201_CREATED)

 