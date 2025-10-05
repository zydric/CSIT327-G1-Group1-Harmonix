from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

# Placeholder views (logic to be implemented in next phase)
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        return Response({"message": "Register endpoint placeholder"})

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        return Response({"message": "Login endpoint placeholder"})

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
