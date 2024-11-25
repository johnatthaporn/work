from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='work/')
    description = models.TextField()
    ownby = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserCart(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)