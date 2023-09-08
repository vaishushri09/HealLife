from django.shortcuts import render, redirect
from .models import Food, Consume
from health_app.models import UserProfile
# Create your views here.


def index(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        foods = Food.objects.all()

    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)

    return render(request, 'myapp/index.html', {'foods': foods, 'consumed_food': consumed_food,'user_profile':user_profile})


def delete_consume(request, id):
    user_profile = UserProfile.objects.get(user=request.user)
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/app')
    return render(request, 'myapp/delete.html',{'user_profile':user_profile})



from django.shortcuts import render, redirect
import requests
from .models import Food

from django.shortcuts import render, redirect
import requests
from .models import Food

def add_food(request):
    if request.method == 'POST':
        food_name = request.POST.get('food_name')
        
        api_url = f'https://api.api-ninjas.com/v1/nutrition?query={food_name}'
        headers = {'X-Api-Key': 'DWuCI3z4Qakky7/FdzHJHg==yRSlXi5uPF9CUECz'}  # Replace with your actual API key
        
        try:
            response = requests.get(api_url, headers=headers)
            if response.status_code == requests.codes.ok:
                food_data_list = response.json()  # Response is a list of food data
                
                if food_data_list:
                    food_data = food_data_list[0]  # Assuming you want to extract the first food entry
                
                    # Create a new Food instance and populate the fields
                    Food.objects.create(
                        name=food_data['name'],
                        carbs=food_data['carbohydrates_total_g'],
                        protein=food_data['protein_g'],
                        fats=food_data['fat_total_g'],
                        calories=food_data['calories']
                    )
                
                    return redirect('add_food')
                else:
                    error_message = "No nutritional information found for the provided food."
                    return render(request, 'myapp/add_food.html', {'error_message': error_message})
            else:
                error_message = f"Error: {response.status_code} - {response.text}"
                return render(request, 'myapp/add_food.html', {'error_message': error_message})
        except requests.exceptions.RequestException as e:
            error_message = f"Error: {e}"
            return render(request, 'myapp/add_food.html', {'error_message': error_message})

    foods = Food.objects.all()  # Fetch all existing food entries
    return render(request, 'myapp/add_food.html', {'foods': foods})




from django.shortcuts import render, redirect
from .models import SleepPattern
from .forms import SleepPatternForm

def view_sleep_patterns(request):
    sleep_patterns = SleepPattern.objects.filter(user=request.user)
    user_profile = UserProfile.objects.get(user=request.user)
    context = {'sleep_patterns': sleep_patterns,'user_profile':user_profile}
    return render(request, 'myapp/view_sleep_patterns.html', context)

def add_sleep_pattern(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = SleepPatternForm(request.POST)
        if form.is_valid():
            sleep_pattern = form.save(commit=False)
            sleep_pattern.user = request.user
            sleep_pattern.save()
            return redirect('x/')
    else:
        form = SleepPatternForm()
    context = {'form': form,'user_profile':user_profile}
    return render(request, 'myapp/add_sleep_pattern.html', context)

from django.shortcuts import render
from .models import SleepPattern
import openai

def suggest_sleep_cycle(request):
    user_profile = UserProfile.objects.get(user=request.user)
    user = request.user  # Assuming you're using authentication
    sleep_patterns = SleepPattern.objects.filter(user=user)

    # Collect user data for the prompt
    prompt = "Based on your sleep patterns, I suggest the following sleep cycle:\n"
    for pattern in sleep_patterns:
        prompt += f"Sleep time: {pattern.start_time.strftime('%Y-%m-%d %H:%M')}, "
        prompt += f"Wake time: {pattern.end_time.strftime('%Y-%m-%d %H:%M')}, "
        prompt += f"Sleep quality: {pattern.get_quality_rating_display()}\n"
    
    prompt += "\nPlease provide a brief sleep cycle suggestion."
    # Set up OpenAI API
    openai.api_key = "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"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=0.7
    )

    suggestion = response.choices[0].text.strip()

    context = {
        "sleep_patterns": sleep_patterns,
        "suggestion": suggestion,
        'user_profile':user_profile
    }

    return render(request, "myapp/suggestions.html", context)

    
def tryi(request):
    return render(request,"myapp/try.html")

from django.shortcuts import render
from .models import Consume, SleepPattern
from datetime import date
from health_app.models import UserProfile
def generate_report(request):
    # Get the user's profile data
    user_profile = UserProfile.objects.get(user=request.user)

    # Get today's date
    today = date.today()

    # Get the user's calorie intake data for today
    calorie_intake_today = Consume.objects.filter(user=request.user, date=today).values_list('food_consumed__calories', flat=True)
    total_calories_today = sum(calorie_intake_today)
    print(total_calories_today)
    rem=2000-total_calories_today
    # Get the user's sleep cycle data
    sleep_patterns = SleepPattern.objects.filter(user=request.user)

    # Prepare data for sleep quality bar chart
    sleep_quality_data = {
        'poor': sleep_patterns.filter(quality_rating=1).count(),
        'fair': sleep_patterns.filter(quality_rating=2).count(),
        'good': sleep_patterns.filter(quality_rating=3).count(),
        'very_good': sleep_patterns.filter(quality_rating=4).count(),
        'excellent': sleep_patterns.filter(quality_rating=5).count(),
    }

    # Data for the pie chart
    pie_chart_data = {
        'Calories Consumed': total_calories_today,
        'Remaining Calories': 2000 - total_calories_today,
    }
    prompt = f"Based on your data: Total calories today: {total_calories_today}, Sleep patterns - Poor: {sleep_quality_data['poor']}, Fair: {sleep_quality_data['fair']}, Good: {sleep_quality_data['good']}, Very Good: {sleep_quality_data['very_good']}, Excellent: {sleep_quality_data['excellent']}, etc. What suggestions can you provide?"

    response = openai.Completion.create(
        engine="text-davinci-002",  # Choose an appropriate engine
        prompt=prompt,
        max_tokens=100,  # Adjust the max_tokens as needed
        n=1
    )

    # Extract the generated suggestions from the GPT-3 response
    suggestions = response.choices[0].text.strip()

    return render(request, 'myapp/report_template.html', {
        'user_profile': user_profile,
        'total_calories_today': total_calories_today,
        'rem':rem,
        'sleep_quality_data': sleep_quality_data,
        'pie_chart_data': pie_chart_data,
        'sleep_patterns':sleep_patterns,
        'suggestions':suggestions,
    })




