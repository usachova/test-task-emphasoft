from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from .models import Room, Booking
from .serializers import RoomSerializer, BookingSerializer

class BookingAPIView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class BookingAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    # permission_classes =

class BookingAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (IsAdminUser, )

class RoomAPIView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    # permission_classes =

class RoomAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    # permission_classes =

class RoomAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = IsAdminUser


