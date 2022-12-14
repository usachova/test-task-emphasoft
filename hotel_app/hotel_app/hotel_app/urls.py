"""hotel_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from booking_app.views import (
    MainView,
    LoginUserView,
    RedistrUserView,
    LogoutUserView,
    RoomAPIView,
    BookingAPIView,
    BookingAPIUpdate,
    BookingAPIDestroy,
    RoomAPISearch,
)

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('login', LoginUserView.as_view(), name='login'),
    path('register', RedistrUserView.as_view(), name='register'),
    path('logout', LogoutUserView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/rooms/', RoomAPIView.as_view()),
    path('api/bookings', BookingAPIView.as_view()),
    path('api/booking/<int:pk>/', BookingAPIUpdate.as_view()),
    path('api/delete_booking/<int:pk>/', BookingAPIDestroy.as_view()),
    path('api/search_room/', RoomAPISearch.as_view())
]
