from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Local(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name