from django.db import models

# Create your models here.



class Laptop(models.Model):
    company_name = models.CharField(max_length=50)
    laptop_name = models.CharField(max_length=50)
    laptop_model = models.CharField(max_length=50)
    laptop_price = models.CharField(max_length=100)


class Mobile(models.Model):
    company_name = models.CharField(max_length=50)
    mobile_name = models.CharField(max_length=50)
    mobile_model = models.CharField(max_length=50)
    mobile_price = models.CharField(max_length=100)


class LED(models.Model):
    company_name = models.CharField(max_length=50)
    LED_name = models.CharField(max_length=50)
    LED_model = models.CharField(max_length=50)
    LED_price = models.CharField(max_length=100)



