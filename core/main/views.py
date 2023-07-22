from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views import View

from main.models import Service, Staff
from .forms import AppointmentForm, ContactForm, StaffForm


class BaseView(View):
    template = "main/base.html"

    def get(self, request, *args, **kwargs):
        services = Service.objects.all()
        context = {
            "services": services,
        }
        return render(request, self.template, context)


class ContactUsView(View):
    def get(self, request, *args, **kwargs):
        return redirect("main:base")

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message Sent Successfully. You will hear from us soon!')  # noqa
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            for k, v in form.errors.items():
                messages.info(request, f'{k}: {v}')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class AppointmentView(View):
    template = "main/appointment.html"

    def get(self, request, *args, **kwargs):
        staffs = Staff.objects.all()
        services = Service.objects.all()
        context = {
            "staffs": staffs,
            "services": services,
        }
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        staff_id = request.POST.get("staff_id")
        service_id = request.POST.get("service_id")
        staff = Staff.objects.filter(id=staff_id).first()
        service = Service.objects.filter(id=service_id).first()
        form = AppointmentForm(request.POST, request.FILES or None)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.staff = staff
            appointment.service = service
            appointment.save()
            messages.success(request, 'Appointment Booked Successfully! We will get back to you')  # noqa
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        for k, v in form.errors.items():
            messages.info(request, f'{k}: {v}')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
