from django.db import models
from django.forms import CharField

# Create your models here.

### About models ######
class About(models.Model):
    desc = models.TextField()
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=12,unique=True)
    dob=models.DateField(max_length=20)
    education=models.TextField()
    city=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    image = models.ImageField(upload_to='images',default="")
    profile_link=models.TextField()

    def __str__(self):
        return self.name

## Contact models #######
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=254)
    education=models.TextField(max_length=254)
    address=models.TextField(max_length=254)
    message=models.TextField(max_length=254)

    def __str__(self):
        return self.email

### Skills ##############

class Skills(models.Model):
    name=models.CharField(max_length=50)
    percentage=models.IntegerField()

    def __str__(self):
        return self.name

### Social Links ###




