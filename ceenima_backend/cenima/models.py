from django.db import models
import random
import string
from django.contrib.auth.models import User



def generate_random_code():
    length = 6

    while(True):
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Shows.objects.filter(title=code).count()== 0:
            break

# Create your models here.
class Shows(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    summary = models.CharField(max_length=50)
    link = models.TextField(max_length=200)
    image_link = models.TextField(max_length=200)
    time_showing = models.DateTimeField( auto_now_add=False)
    second_time_showing = models.DateTimeField(auto_now_add=False)
    third_time_showinng = models.DateTimeField(auto_now_add=False)
    fourth_time_showing = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.title

class Cenima_Show(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    summary = models.CharField(max_length=50)
    link = models.TextField(max_length=200)
    location = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_link = models.TextField(max_length=200)
    time_showing = models.TimeField( auto_now_add=False)
    second_time_showing = models.TimeField(auto_now_add=False)
    third_time_showing = models.TimeField(auto_now_add=False)
    fourth_time_showing = models.TimeField(auto_now_add=False)
    date_showing = models.DateTimeField( auto_now_add=False)
    second_date_showing = models.DateTimeField(auto_now_add=False)
    third_date_showing = models.DateTimeField(auto_now_add=False)
    fourth_date_showing = models.DateTimeField(auto_now_add=False)


    def __str__(self):
        return self.title


#import mapped a created model class to a User django model.. Inheriting the user class creates multiple instances
class UserInfo(models.Model):

    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic =models.ImageField(upload_to='profile_pic', blank=True)

    def __str__(self):
        return self.user.username


#images of movies that just arrived
class New_movies(models.Model):

    new_pic = models.ImageField(upload_to='new_movies_pics', blank=True)



# images of upcomig movies
class Upcoming_Movies(models.Model):

    upcoming_pic =models.ImageField(upload_to='upcoming_movie_img', blank=True)

    


#Transaction details
class Transaction(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    transaction_name = models.CharField(max_length=50)
    transaction_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tickets_quantity = models.IntegerField()
    location =models.TextField(max_length=200)

    def __str__(self):
        return self.user.username, self.transaction_name, self.price, self.tickets_quantity, self.location

