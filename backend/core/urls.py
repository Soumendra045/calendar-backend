from django.urls import path
# from rest_framework import permissions

from .views import (
    AppointmentCreateView,
    AppointmentListOwnView,
    AppointmentListAllView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,     
)

from .views import RegisterView


urlpatterns = [
    path("appointments/", AppointmentCreateView.as_view(), name="create-appointment"),
    path("appointments/mine/", AppointmentListOwnView.as_view(), name="my-appointments"),
    path("appointments/all/", AppointmentListAllView.as_view(), name="all-appointments"),


    path("auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    #register user
    path("auth/register/", RegisterView.as_view(), name="user_register"),

]

