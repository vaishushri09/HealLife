from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cal/', views.calorie_calculator, name='calorie_calculator'),
]
