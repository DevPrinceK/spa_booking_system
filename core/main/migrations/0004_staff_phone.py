# Generated by Django 4.2.3 on 2023-07-22 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_appointment_date_appointment_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="staff",
            name="phone",
            field=models.CharField(default="0505757031", max_length=15),
        ),
    ]
