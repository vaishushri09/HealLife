from django.contrib import admin
from .models import Food, Consume,SleepPattern

# Register your models here.
admin.site.register(Food)
admin.site.register(Consume)
admin.site.register(SleepPattern)
