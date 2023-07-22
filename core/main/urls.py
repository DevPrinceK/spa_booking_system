from django.urls import path
from .views import *


app_name = "main"
urlpatterns = [
    path('', BaseView.as_view(), name="base"),
    path('contact-us/', ContactUsView.as_view(), name="contact_us"),
    path('book-appointment/', AppointmentView.as_view(), name="appointment"),  # noqa
]
