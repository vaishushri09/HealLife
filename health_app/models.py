from django.db import models

class Exercise(models.Model):
    date = models.DateField()
    duration_minutes = models.PositiveIntegerField()
    # Other fields...

class Diet(models.Model):
    date = models.DateField()
    calories_consumed = models.PositiveIntegerField()
    # Other fields...

class Sleep(models.Model):
    date = models.DateField()
    hours_slept = models.DecimalField(max_digits=4, decimal_places=2)
    # Other fields...

class Emotion(models.Model):
    date = models.DateField()
    emotion_type = models.CharField(max_length=20)
    # Other fields...

# Define other models as needed...
# health_app/models.py

# models.py
from django.db import models

class Diets(models.Model):
    calories = models.PositiveIntegerField()
    protein = models.PositiveIntegerField()
    carbohydrates = models.PositiveIntegerField()
    fats = models.PositiveIntegerField()
    recommendation = models.TextField(blank=True, null=True)


from django.contrib.auth.models import User


    # Add additional fields like age, gender, etc.
class UserHealthData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    data = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.timestamp}"

from django.contrib.auth.models import User
from django.db import models

from django.db import models
from django.contrib.auth.models import User 


# Define a function to set the default profile image path
def default_profile_image_path():
    return 'profile_images/default_image.png'  # Adjust the path as needed

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='')
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male')
    contact_no = models.CharField(max_length=15, default='')
    blood_group = models.CharField(max_length=5, default='')
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=None)
    height_cm = models.PositiveIntegerField(null=True, blank=True, default=None)
    # Add other health-related fields here

    # Add an image field for user profile pictures with a default value
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True, default=default_profile_image_path)

    def __str__(self):
        return self.user.username
    
    
from django.contrib.auth.models import User
from django.db import models

class HealthReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    calorie_intake = models.PositiveIntegerField(default=0)
    sleep_duration_minutes = models.PositiveIntegerField(default=0)
    # Add other health-related fields here

    def __str__(self):
        return f"Health Report for {self.user.username} on {self.date}"
