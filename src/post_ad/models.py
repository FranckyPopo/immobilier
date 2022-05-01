from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from authentication.models import User

class City(models.Model):
    city = models.CharField(max_length=20)  
    
    def __str__(self):
        return self.city  

class House(models.Model):
    house = models.CharField(max_length=20)
    
    def __str__(self):
        return self.house  
    
class PostAd(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    
    title_ad = models.CharField(max_length=30)
    description_ad = models.TextField(max_length=1000)
    price_ad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1_000_000_000)])
    photo_ad = models.ImageField()
    
    date_create_ad = models.DateTimeField(auto_now=timezone.now(), blank=True, verbose_name="Date création")
    date_modified_ad = models.DateTimeField(auto_now=True)    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_ad  