from django.db import models
from django.contrib.auth.models import User


class user_table(models.Model):
    fname = models.CharField(max_length=60)
    lname = models.CharField(max_length=60)
    email = models.EmailField()
    DOB = models.DateField()

    def __str__(self):
        return self.fname + " " + self.lname


class User_profileinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_url = models.URLField(blank=True)
    profile_img = models.ImageField(upload_to='profile_pic', blank=True)

    def __str__(self):
        return self.user.username


class User_details(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return self.name
