# blueyonder_hotels/serializers.py
from rest_framework import serializers
from .models import Hotel, Reservations, Room

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'location', 'number_of_rooms']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'hotel', 'room_type', 'is_available', 'capacity', 'price']

class ReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = '__all__'

