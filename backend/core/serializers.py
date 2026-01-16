from rest_framework import serializers
from django.utils import timezone
from .models import Appointment
from django.contrib.auth import get_user_model
from .tasks import notify_appointment_created

User = get_user_model()

from rest_framework import serializers
from django.utils import timezone
from .models import Appointment

class AppointmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ("id", "start_time", "end_time")

    def validate(self, data):
        request = self.context["request"]
        user = request.user

        start_time = data['start_time']
        end_time = data['end_time']

        if start_time >= end_time:
            raise serializers.ValidationError("End time must be after start time.")

        if start_time <= timezone.now():
            raise serializers.ValidationError("Appointment must be in the future.")

        overlapping = Appointment.objects.filter(
            user=user,
            start_time__lt=end_time,
            end_time__gt=start_time
        )
        if overlapping.exists():
            raise serializers.ValidationError("This time slot overlaps with an existing appointment.")

        return data

    def create(self, validated_data):
        request = self.context["request"]
        appointment = Appointment.objects.create(user=request.user, **validated_data)

        #Triggered background task when created
        notify_appointment_created.delay(
        user_email=request.user.email,
        start_time=appointment.start_time.isoformat(),
        end_time=appointment.end_time.isoformat()
    )
        return appointment
    
class AppointmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ("id", "start_time", "end_time", "created_at")

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ("email", "username", "password")
    
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user