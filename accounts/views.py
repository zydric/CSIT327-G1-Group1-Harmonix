from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model, authenticate, login


# Create your views here.
def register(request):
    return render(request, 'accounts/register.html')

def login(request):
    return render(request, 'accounts/login.html')


User = get_user_model()

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    role = request.data.get('role')
    
    if role not in ['musician', 'band_admin']:
        return Response({'error': 'Invalid role selected'}, status=400)
    
    if User.objects.filter(email=email).exists():
        return Response({'error': 'Email already exists'}, status=400)
    
    user = User.objects.create_user(username=username, email=email, password=password, role=role)
    return Response({'success': True, 'user_id': user.id}, status=201)

# @api_view(['POST'])
# def login_view(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
    
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return Response({'success': True, 'role': user.role, 'redirect': '/dashboard'}, status=200)
#     else:
#         return Response({'error': 'Invalid credentials'}, status=400)



# @api_view(['POST'])
# def login_view(request):
#     username = request.data.get("username")
#     password = request.data.get("password")

#     if not username or not password:
#         return Response({"success": False, "error": "Username and password required"}, status=400)

#     user = authenticate(username=username, password=password)
#     if user is not None:
#         return Response({"success": True, "username": user.username})
#     else:
#         return Response({"success": False, "error": "Invalid credentials"}, status=401)


@api_view(['POST'])
def login_view(request):
    try:
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"success": False, "error": "Username and password required"}, status=400)

        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({"success": True, "username": user.username})
        else:
            return Response({"success": False, "error": "Invalid credentials"}, status=401)
    except Exception as e:
        return Response({"success": False, "error": str(e)}, status=500)