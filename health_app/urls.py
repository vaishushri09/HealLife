from django.urls import path,include
from . import views



urlpatterns = [
    path('track/', views.health_tracker_view, name='track'),
    path('responses/', views.responses_view, name='responses'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('main/', views.homepage, name='homepage'),
    path('activity/', views.activity_calories, name='activity_calories'),
    path('cal/', views.calorie_calculator, name='calorie_calculator'),
    path('', views.index_view1, name='index1'),
    path('welcome/', views.index_view, name='index'),
    path('profile/', views.view_profile, name='view_profile'),
    path('login/profile/edit/', views.edit_profile, name='edit_profile'),
    
]
