


from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from .models import Laptop, Mobile, LED  # Import your models
from .serializers import LaptopSerializer, MobileSerializer, LEDSerializer  # Import your serializers
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import generics
from .models import Laptop
from .serializers import LaptopSerializer


class LaptopListCreate(ListCreateAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer



class LaptopCreateView(generics.CreateAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer

# views.py


class LaptopDelete(generics.DestroyAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer


class MobileListCreate(ListCreateAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer

class MobileDelete(DestroyAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer

class LEDListCreate(ListCreateAPIView):
    queryset = LED.objects.all()
    serializer_class = LEDSerializer

class LEDDelete(DestroyAPIView):
    queryset = LED.objects.all()
    serializer_class = LEDSerializer












@api_view(['GET'])
def check_auth(request):
    if request.user.is_authenticated:
        return Response({"user": request.user.username}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def login_page(request):
    if request.method == "POST":
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not User.objects.filter(username=username).exists():
            return Response({"error": "Invalid Username"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            return Response({"error": "Invalid Password"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            login(request, user)
            return Response({"message": "Login successful", "user": username}, status=status.HTTP_200_OK)

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
from django.contrib.auth.models import User

@api_view(['POST'])
def register_page(request):
    if request.method == 'POST':
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        username = request.data.get('username')
        password = request.data.get('password')
        
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create a new user with appropriate permissions
        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
        user.is_staff = True
        user.is_superuser = True   # or user.is_superuser = True if needed
        user.save()

        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
