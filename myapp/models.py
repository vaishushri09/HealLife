from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Food(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()

import datetime 
class Consume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)  # Import datetime at the beginning

    def __str__(self):
        return f"{self.user.username} - {self.date}"



class SleepPattern(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    quality_rating = models.PositiveIntegerField(choices=[
        (1, 'Poor'),
        (2, 'Fair'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent')
    ])

    def __str__(self):
        return f"Sleep Pattern for {self.user.username}"





