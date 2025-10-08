from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from django.contrib.auth import login as django_login
from .serializers import RegistrationSerializer, LoginSerializer


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.save()

        django_login(request, user)

        response_data = {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "role": user.role,
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.validated_data["user"]
        django_login(request, user)

        return Response({
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "role": user.role,
        }, status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        return Response({"message": "Logout endpoint placeholder"})


class MusicianProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        return Response({"message": f"View musician profile {pk} placeholder"})


class BandProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        return Response({"message": f"View band profile {pk} placeholder"})


class ListingListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "List all listings placeholder"})

    def post(self, request):
        return Response({"message": "Create listing placeholder"})


class ListingDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        return Response({"message": f"Get listing {pk} placeholder"})


