from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo')
)

DAYS_OF_THE_WEEK = (
    ('monday', 'Lunes'),
    ('tuesday', 'Martes'),
    ('wednesday', 'Miércoles'),
    ('thursday', 'Jueves'),
    ('friday', 'Viernes'),
    ('saturday', 'Sábado'),
    ('sunday', 'Domingo'),
)


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_description = models.TextField(max_length=500, blank=True, null=True)
    status = models.TextField(max_length=20, choices=STATUS_CHOICES, default='Active')
    local_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    category_featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d',blank=True, null=True)
    available_days = models.JSONField(default=list, blank=True, null=True)
    available_time_start = models.TimeField(blank=True, null=True)
    available_time_end = models.TimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.category_name


class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    local_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product_description = models.TextField(max_length=500)
    status = models.TextField(max_length=20, choices=STATUS_CHOICES, default='Active')
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    product_featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d',blank=True, null=True)
    available_days = models.JSONField(default=list, blank=True, null=True)
    available_time_start = models.TimeField(blank=True, null=True)
    available_time_end = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.product_name





