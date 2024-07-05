# HBSApp/views.py
from rest_framework import generics, status
from django.http import JsonResponse
from rest_framework.response import Response
from .models import Hotel, Room, Reservations
from .serializers import HotelSerializer, ReservationsSerializer, RoomSerializer
from django.utils import timezone

# @csrf_exempt
# def user_signup(request):
#     if request.method =="POST":
#         # if 'username' not in request.json() or 'password1' not in request.POST or 'password2' not in request.POST:
#         #     return JsonResponse({"error": "Missing required parameters"}, status=400)
    
#         user_name = request.json.get['username']
#         password1 = request.json.get['password1']
#         password2 = request.json.get['password2']
#         if password1 != password2:
#             return JsonResponse({"error": "Passwords do not match"}, status=400)
#         try:
            
#             if User.objects.filter(username=user_name).exists():
#                 return JsonResponse({"error": "Username not available. Please choose another."}, status=400)
            
            
        
#         except Exception as e:
#             return JsonResponse({"error1": f"Error occurred: {str(e)}"}, status=500)
#         new_user = User.objects.create_user(username=user_name, password=password1)
#         new_user.is_superuser = False
#         new_user.is_staff = False
#         new_user.save()
        
#         return JsonResponse({"message": "User created successfully"}, status=201)

#     return JsonResponse({"error2": "Invalid Method"}, status=405)

# @csrf_exempt
# def user_login(request):
#     if request.method == 'POST':
#         try:
#             username = request.POST['username']
#             password = request.POST['password']

#             user = authenticate(username=username, password=password)
            
#             if user is not None:
#                 token, created = Token.objects.get_or_create(user=user)
#                 return JsonResponse({"message": f"Successfully logged in. Token: {token.key}"}, status=200)
#             else:
#                 return JsonResponse({"error": "Incorrect username or password"}, status=400)
        
#         except Exception as e:
#             return JsonResponse({"error": f"Error occurred: {str(e)}"}, status=500)

#     return JsonResponse({"error": "Invalid Method"}, status=405)

class HotelListCreateView(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    
    def create(self, request, *args, **kwargs):
        location = request.data.get('location')
        if Hotel.objects.filter(location=location).exists():
            return Response({"error": f"Hotel with location '{location}' already exists."}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

# class UserListView(generics.ListAPIView):
#     queryset =  User.objects.all()
#     serializer_class = UserSerializer

class HotelUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    lookup_field = 'location'

class HotelListView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def create(self, request, *args, **kwargs):
        hotel_id = request.data.get('hotel')
        room_type = request.data.get('room_type')

        try:
            hotel_instance = Hotel.objects.get(id=hotel_id)
        except Hotel.DoesNotExist:
            return Response({"error": f"Hotel with id '{hotel_id}' does not exist."}, status=status.HTTP_404_NOT_FOUND)

        existing_rooms_count = Room.objects.filter(hotel=hotel_instance).count()
        if existing_rooms_count >= hotel_instance.number_of_rooms:
            return Response({"error": "Cannot create more rooms, limit crossed."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoomListByHotelView(generics.ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        location = self.kwargs['location']
        hotel = Hotel.objects.get(location=location)
        return Room.objects.filter(hotel=hotel)
    
class ReservationsCheckAvailabilityView(generics.ListAPIView):
    serializer_class = ReservationsSerializer
    # permission_classes = [permissions.IsAuthenticated]  # Ensure only authenticated users can access

    def get_queryset(self):
        location = self.request.query_params.get('location')
        checkin_date = self.request.query_params.get('checkin_date')
        checkout_date = self.request.query_params.get('checkout_date')
        number_of_people = self.request.query_params.get('number_of_people')

        # Query rooms based on location, availability, and capacity
        rooms_available = Room.objects.filter(
            hotel__location=location,
            is_available=True,
            capacity__gte=number_of_people
        )

        return rooms_available

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = RoomSerializer(queryset, many=True)  # Serialize queryset
        response_data = {
            "total_rooms_available": queryset.count(),
            "rooms": serializer.data  # Include serialized room details in response
        }
        return Response(response_data)

class ReservationCreateView(generics.CreateAPIView):
    serializer_class = ReservationsSerializer

    def create(self, request, *args, **kwargs):
        room_id = request.data.get('room')
        checkin_date = request.data.get('checkin_date')
        checkout_date = request.data.get('checkout_date')
        number_of_people = request.data.get('number_of_people')
        location = request.data.get('location')

        # Check if the room exists and belongs to a hotel with enough capacity
        try:
            room_instance = Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            return Response({"error": f"Room with id '{room_id}' does not exist."}, status=status.HTTP_404_NOT_FOUND)

        # Check if the hotel associated with the room has enough capacity
        if number_of_people >= room_instance.capacity:
            return Response({"error": "Hotel has reached its room capacity limit."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the room is already booked for the specified dates
        if Reservations.objects.filter(
            room=room_instance,
            checkout_date__gte=checkin_date,
            checkin_date__lte=checkout_date
        ).exists():
            return Response({"error": "Room is already booked for the specified dates."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if room capacity is sufficient for the specified number of people
        if room_instance.capacity < number_of_people:
            return Response({"error": "Room capacity is insufficient for the specified number of people."}, status=status.HTTP_400_BAD_REQUEST)

        # All checks passed, create the reservation
        serializer = ReservationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReservationListView(generics.ListAPIView):
    queryset = Reservations.objects.all()
    serializer_class = ReservationsSerializer