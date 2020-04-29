from django.db import models


class Classified(models.Model):
    CATEGORIES = [
        ('auto', 'Auto'),
        ('free', 'Free'),
        ('furniture', 'Furniture'),
        ('household', 'Household'),
        ('other', 'Other'),
        ('room-for-rent', 'Room For Rent'),
        ('sporting', 'Sporting'),
        ('wanted', 'Wanted')
    ]
    DAYS_LISTED = [
        ('7', '7 Days'),
        ('14', '14 Days'),
        ('21', '21 Days')
    ]
    category = models.CharField(choices=CATEGORIES, max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    location = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)
    days_listed = models.CharField(choices=DAYS_LISTED, max_length=2)
    pictures = models.ImageField(upload_to='images/', blank=True, null=True)
