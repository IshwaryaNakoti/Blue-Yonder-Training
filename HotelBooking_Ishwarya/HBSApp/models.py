from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hotel(models.Model):
    CAPITAL_CITIES = [
        ('Hyderabad', 'Hyderabad'),
        ('Bangalore', 'Bangalore'),
        ('Mumbai', 'Mumbai'),
        ('Jaipur', 'Jaipur'),
        ('Chennai', 'Chennai'),
        ('Kolkata', 'Kolkata'),
        ('Lucknow', 'Lucknow'),
        ('Bhopal', 'Bhopal'),
        ('Chandigarh', 'Chandigarh'),
        ('Raipur', 'Raipur'),
    ]

    location = models.CharField(max_length=50, choices=CAPITAL_CITIES, unique=True)
    number_of_rooms = models.PositiveIntegerField()

    def __str__(self):
        return self.location
    
class Room(models.Model):
    ROOM_TYPES = [
        ('Premium', 'Premium'),
        ('Deluxe', 'Deluxe'),
        ('Basic', 'Basic'),
    ]

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=50, choices=ROOM_TYPES)
    is_available = models.BooleanField(default=True)
    capacity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if Room.objects.filter(hotel=self.hotel).count() >= self.hotel.number_of_rooms:
            raise ValueError("Cannot create more rooms, limit crossed.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.hotel.location} - {self.room_type}"

class Reservations(models.Model):
    LOCATION_CHOICES = [
        ('Hyderabad', 'Hyderabad'),
        ('Bangalore', 'Bangalore'),
        ('Mumbai', 'Mumbai'),
        ('Jaipur', 'Jaipur'),
        ('Chennai', 'Chennai'),
        ('Kolkata', 'Kolkata'),
        ('Lucknow', 'Lucknow'),
        ('Bhopal', 'Bhopal'),
        ('Chandigarh', 'Chandigarh'),
        ('Raipur', 'Raipur'),
    ]

    location = models.CharField(max_length=50, choices=LOCATION_CHOICES)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    number_of_people = models.PositiveIntegerField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.location} - {self.checkin_date} to {self.checkout_date}"