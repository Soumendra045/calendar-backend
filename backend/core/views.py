from .models import Appointment
from .serializers import AppointmentCreateSerializer, AppointmentListSerializer, UserRegisterSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from .permissions import IsAdmin, IsUser

class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]



# USER: Create Appointment
class AppointmentCreateView(generics.CreateAPIView):
    serializer_class = AppointmentCreateSerializer
    permission_classes = [IsAuthenticated, IsUser]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})

        return context
    
#user: list own Appointment
class AppointmentListOwnView(generics.ListAPIView):
    serializer_class = AppointmentListSerializer
    permission_classes = [IsAuthenticated, IsUser]

    def get_queryset(self):
        return Appointment.objects.filter(user=self.request.user)


#List For admin users
class AppointmentListAllView(generics.ListAPIView):
    serializer_class = AppointmentListSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def get_queryset(self):
        return Appointment.objects.all()   


