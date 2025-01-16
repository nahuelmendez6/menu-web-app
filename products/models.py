from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

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

class AvailabilityMixin(models.Model):
    available_days = models.JSONField(default=list, blank=True, null=True)
    available_time_start = models.TimeField(blank=True, null=True)
    available_time_end = models.TimeField(blank=True, null=True)

    class Meta:
        abstract = True

    def clean(self):
        if self.available_time_start and self.available_time_end:
            if self.available_time_start >= self.available_time_end:
                raise ValidationError("La hora de inicio debe ser anterior a la hora de finalización")

    def is_available(self, day, time=None):
        if day not in self.available_days:
            return False
        if time:
            if self.available_time_start and time < self.available_time_start:
                return False
            if self.available_time_end and time > self.available_time_end:
                return False

        return True


# Create your models here.
class Category(models.Model, AvailabilityMixin):
    category_name = models.CharField(max_length=100)
    category_description = models.TextField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    local_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    featured_image = models.ImageField(upload_to='uploads/',blank=True, null=True)


    class Meta:
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.category_name


class Product(models.Model, AvailabilityMixin):
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products') # category.products.all()
    local_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product_description = models.TextField(max_length=500)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    featured_image = models.ImageField(upload_to='uploads/',blank=True, null=True)

    class Meta:
        verbose_name_plural = 'productos'

    def __str__(self):
        return self.product_name





