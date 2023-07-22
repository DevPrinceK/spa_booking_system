from django.db import models


class Staff(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, default="0505757031")
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to="staff/")
    description = models.TextField()

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="services/")

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15)
    service_type = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, null=True, blank=True)
    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE,  null=True, blank=True)

    def __str__(self) -> str:
        return self.customer_name
