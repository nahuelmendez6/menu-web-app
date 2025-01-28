from django.contrib.auth.models import User
from django.db import models

DAYS_OF_THE_WEEK = (
    ('monday', 'Lunes'),
    ('tuesday', 'Martes'),
    ('wednesday', 'Miércoles'),
    ('thursday', 'Jueves'),
    ('friday', 'Viernes'),
    ('saturday', 'Sábado'),
    ('sunday', 'Domingo'),
)

HOURS_OF_THE_DAY = (
    '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00',
    '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00',
)


class Address(models.Model):
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    street_number = models.CharField(max_length=50)

# Create your models here.
class Business(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='locals')
    name = models.CharField(max_length=100)
    days = models.JSONField(default=list, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='address')
    fst_opening_time = models.TimeField(blank=True, null=True)
    fst_closing_time = models.TimeField(blank=True, null=True)
    snd_opening_time = models.TimeField(blank=True, null=True)
    snd_closing_time = models.TimeField(blank=True, null=True)