from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('activity/', views.activity_calories, name='activity_calories'),
    path('cal/', views.calorie_calculator, name='calorie_calculator'),
    path('exe/', views.exercise_nutrition, name='calorie_calculator'),
    
]
