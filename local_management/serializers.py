from rest_framework import serializers
from .models import Address, Business

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['country', 'state', 'dapartment', 'city', 'street', 'street_number']


class Busi