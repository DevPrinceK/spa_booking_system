import array

import requests
# from core import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
import core.settings as settings
from .models import Contact, Appointment, Staff


@receiver(post_save, sender=Contact)
def notify_about_contact(sender, instance, created, **kwargs):
    staffs = Staff.objects.all()
    # make a list of all phone numbers of staff members
    recipients = [staff.phone for staff in staffs]
    if created:
        send_sms(settings.SMS_SENDER_ID,
                 f"New contact from {instance.name} with email {instance.email}\n{instance.message} ", recipients)


@receiver(post_save, sender=Appointment)
def notify_about_appointment(sender, instance, created, **kwargs):
    staffs = Staff.objects.all()
    # make a list of all phone numbers of staff members
    staff_recipients = [staff.phone for staff in staffs]
    customer_receipient = [str(instance.customer_phone)]
    staff_message = f"New appointment from {instance.customer_name} with email {instance.customer_email} for {instance.service}({instance.service_type}) on {instance.date} at {instance.time}"
    customer_message = f"Dear {instance.customer_name}, your appointment for {instance.service}({instance.service_type}) on {instance.date} at {instance.time} has been received. We will get back to you shortly."
    if created:
        # send to staff
        send_sms(settings.SMS_SENDER_ID, staff_message, staff_recipients)
        # send to customer
        send_sms(settings.SMS_SENDER_ID, customer_message, customer_receipient)


def send_sms(sender: str, message: str, recipients: array.array):
    header = {"api-key": settings.ARKESEL_API_KEY, 'Content-Type': 'application/json',
              'Accept': 'application/json'}
    SEND_SMS_URL = "https://sms.arkesel.com/api/v2/sms/send"
    payload = {
        "sender": sender,
        "message": message,
        "recipients": recipients
    }
    response = requests.post(SEND_SMS_URL, headers=header, json=payload)
    print(response.json())
    return response.json()
