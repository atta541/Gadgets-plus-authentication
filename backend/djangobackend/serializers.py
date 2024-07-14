from rest_framework import serializers
from .models import Laptop, Mobile, LED

# serializers.py
# serializers.py
# serializers.py
from rest_framework import serializers
from .models import Laptop

class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = ['id', 'company_name', 'laptop_name', 'laptop_model', 'laptop_price']


class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = '__all__'

class LEDSerializer(serializers.ModelSerializer):
    class Meta:
        model = LED
        fields = '__all__'





