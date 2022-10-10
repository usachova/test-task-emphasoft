from datetime import timezone, datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client, RequestFactory

from booking_app.models import Room, Booking
from booking_app.views import RoomAPIView, BookingAPIView


# Create your tests here.
class RoomTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_user('testuser', 'testuder@vk.ru', 'testpassword')
        self.test_user.is_superuser = True
        self.test_user.is_active = True
        self.test_user.save()
        self.assertEqual(self.test_user.is_superuser, True)
        login = self.client.login(username='testuser', password='testpassword')
        self.failUnless(login, 'Could not log in')
        Room.objects.create(number='1', cost=1000, beds_count=3)

    def test_room_create_view(self):
        request = RequestFactory().get('/api/rooms/')
        view = RoomAPIView()
        view.request = request
        self.assertQuerysetEqual(view.get_queryset(), Room.objects.all())

    def test_room_search_view(self):
        request = RequestFactory().get('/api/search_room/?date_start=2022-10-10&date_finish=2022-10-22')
        view = RoomAPIView()
        view.request = request
        self.assertQuerysetEqual(view.get_queryset(), Room.objects.all())


class BookingTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_user('testuser', 'testuder@vk.ru', 'testpassword')
        self.test_user.is_superuser = True
        self.test_user.is_active = True
        self.test_user.save()
        self.assertEqual(self.test_user.is_superuser, True)
        login = self.client.login(username='testuser', password='testpassword')
        self.failUnless(login, 'Could not log in')
        Room.objects.create(number='1', cost=1000, beds_count=3)

    def test_booking_create_view(self):
        self.client.post('/api/bookings', {'date_start': '2022-10-11', 'date_finish': '2022-10-12',
                                                          'room': 1, 'user': self.test_user.id})
        self.assertEqual(Booking.objects.count(), 1)
