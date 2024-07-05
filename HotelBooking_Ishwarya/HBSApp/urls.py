"""
URL configuration for HotelBooking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# HBSApp/urls.py
# blueyonder_hotels/urls.py
from django.urls import path
from .views import HotelListCreateView, RoomListCreateView, RoomListByHotelView, HotelUpdateView, HotelListView, ReservationsCheckAvailabilityView, ReservationCreateView, ReservationListView
urlpatterns = [
    path('hotels/', HotelListCreateView.as_view(), name='hotel-list-create'),
    path('hotels/all/', HotelListView.as_view(), name='hotel-list'),
    path('hotels/<str:location>/', HotelUpdateView.as_view(), name='hotel-update'),
    path('rooms/', RoomListCreateView.as_view(), name='room-list-create'),
    path('rooms/<str:location>/', RoomListByHotelView.as_view(), name='room-list-by-hotel'),
    path('reservations/check_availability/', ReservationsCheckAvailabilityView.as_view(), name='check-availability'),
    path('book-room/', ReservationCreateView.as_view(), name="BookRoom"),
    path('bookings/', ReservationListView.as_view(), name='bookings')

]