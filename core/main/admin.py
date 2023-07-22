from django.contrib import admin
from .models import *


admin.AdminSite.site_title = "UltraSpa Spa and Salon"
admin.AdminSite.site_header = "UltraSpa Spa and Salon"


class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone"]


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["customer_name", "customer_phone", "customer_email", "service_type", "date", "time"]  # noqa


class StaffAdmin(admin.ModelAdmin):
    list_display = ["name", "position"]


admin.site.register(Service)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Staff, StaffAdmin)
