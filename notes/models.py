from django.db import models
from django.contrib.auth.models import User



class Dog(models.Model):
    owner = models.ForeignKey(User, related_name='dogs', on_delete=models.CASCADE, default=1)  # Set default owner ID
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    available_for_adoption = models.BooleanField(default=False)
    image = models.ImageField(upload_to='dog_images/', blank=True, null=True)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.name

    
