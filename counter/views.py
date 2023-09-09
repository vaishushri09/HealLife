from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': 'DWuCI3z4Qakky7/FdzHJHg==yRSlXi5uPF9CUECz'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})

import requests
from django.shortcuts import render

@login_required
def activity_calories(request):
    activity = 'cycling'
    api_url = 'https://api.api-ninjas.com/v1/caloriesburned?activity={}'.format(activity)
    response = requests.get(api_url, headers={'X-Api-Key': 'DWuCI3z4Qakky7/FdzHJHg==yRSlXi5uPF9CUECz'})

    if response.status_code == requests.codes.ok:
        data = response.json()
        print(data)
    else:
        data = []

    return render(request, 'activity_calories.html', {'activity_data': data})

from django.shortcuts import render
import json
import requests

from django.shortcuts import render
import json
import requests

@login_required
def calorie_calculator(request):
    total_calories = None

    if request.method == 'POST':
        query = request.POST.get('query')
        food_items = [item.strip() for item in query.split(',')]

        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='

        total_calories = 0
        

        for item in food_items:
            api_request = requests.get(
                api_url + item, headers={'X-Api-Key': 'DWuCI3z4Qakky7/FdzHJHg==yRSlXi5uPF9CUECz'})
            print(f"API URL for {item}: {api_request.url}")  # Check the URL being requested
            print(f"API response for {item}: {api_request.content}") 
            print(f"data{item}:{api_request.content[1]}")
            api_response = api_request.content.decode('utf-8')
            api_data = json.loads(api_response)
            print(api_data)
            total_calories += float(api_data[0].get('calories', 0))
            print(total_calories)
            

    return render(request, 'calorie_calculator.html', {'total_calories': total_calories})

from django.shortcuts import render
import requests
import json

@login_required
def exercise_nutrition(request):
    if request.method == 'POST':
        exercise_name = request.POST.get('exercise_name')
        api_url = f'https://api.api-ninjas.com/v1/exercises?muscle={exercise_name}'
        response = requests.get(api_url, headers={'X-Api-Key': 'DWuCI3z4Qakky7/FdzHJHg==yRSlXi5uPF9CUECz'})

        if response.status_code == requests.codes.ok:
            api_data = json.loads(response.content.decode('utf-8'))
            exercise_info = api_data[0] if api_data else None
        else:
            exercise_info = None

        return render(request, 'exercise_nutrition.html', {'exercise_info': exercise_info})
    return render(request, 'exercise_nutrition.html')
