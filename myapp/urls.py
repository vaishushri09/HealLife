"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from myapp import views
from health_app.views import index_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('try/', views.tryi, name="tryi"),
    path('delete/<int:id>/', views.delete_consume, name="delete"),
    path('add_food/', views.add_food, name='add_food'),
    path('sleep/view/', views.view_sleep_patterns, name='view_sleep_patterns'),
    path('sleep/add/x/', views.view_sleep_patterns, name='view_sleep_patterns'),
    path('sleep/add/', views.add_sleep_pattern, name='add_sleep_pattern'),
    path('suggest_sleep_cycle/', views.suggest_sleep_cycle, name='suggest_sleep_cycle'),
    path('generate-report/', views.generate_report, name='generate-report'),
    path('welcome/', index_view, name='welcome'),
]
urlpatterns += staticfiles_urlpatterns()
