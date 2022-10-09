from datetime import datetime

from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from rest_framework import generics, status
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView

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
    serializer_class = BookingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user.id)

    def post(self, request, *args, **kwargs):
        if Booking.objects.filter(room=request.POST.get('room')).filter(Q(date_start__lte=request.POST.get('date_finish')) |
                                                            Q(date_finish__gte=request.POST.get('date_start'))):
            return Response({'detail': "нельзя забронировать комнату на эти даты"})
        if request.POST.get('date_finish') < request.POST.get('date_start'):
            return Response({'detail': "дата финиша раньше даты старта"})
        return self.create(request, *args, **kwargs)

class BookingAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (IsOwnerOrAdminOrReadOnly, )

class BookingAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (IsOwnerOrAdminOrReadOnly, )

class RoomAPIView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = RoomFilter
    ordering_fields = ['cost', 'beds_count']
    permission_classes = (IsAdminOrReadOnly, )

class RoomAPISearch(APIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

    def get(self, request):
        date_start = datetime.strptime(self.request.GET.get('date_start'), '%Y-%m-%d')
        date_finish = datetime.strptime(self.request.GET.get('date_finish'), '%Y-%m-%d')
        rooms = Room.objects.all()
        queryset = []
        if date_start and date_finish:
            for room in rooms:
                if not room.booking_set.filter(Q(date_start__lte=date_start) | Q(date_finish__gte=date_finish)):
                    queryset.append(room.number)
        else:
            queryset = [room.number for room in rooms]
        return Response(queryset)
