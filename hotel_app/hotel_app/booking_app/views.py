from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Room, Booking
from .permissions import IsOwnerOrAdminOrReadOnly, IsAdminOrReadOnly
from .serializers import RoomSerializer, BookingSerializer
from .service import RoomFilter
from .forms import AuthUserForm, RedistrUserForm

class MainView(View):
    def get(self, request, *args, **kwargs):
        rooms = Room.objects.all()
        return render(request, 'booking_app/index.html', context={'rooms': rooms})

class LoginUserView(LoginView):
    template_name = 'booking_app/login.html'
    form_class = AuthUserForm
    success_url = '/'

    def get_success_url(self):
        return self.success_url

class RedistrUserView(CreateView):
    model = User
    template_name = 'booking_app/register.html'
    success_url = '/'
    form_class = RedistrUserForm

class LogoutUserView(LogoutView):
    next_page = '/'
class BookingAPIView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class BookingAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (IsOwnerOrAdminOrReadOnly, )

class BookingAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (IsOwnerOrAdminOrReadOnly, )

# class BookingAPIFilters():

class RoomAPIView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = RoomFilter
    permission_classes = (IsAdminOrReadOnly, )
