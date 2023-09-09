import openai
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from health_app.models import UserProfile

def is_health_related(reply):
    health_keywords = ["health", "medical", "doctor", "symptom", "illness", "wellness", "nutrition", "diet", "exercise", "healthy", "well-being"]  # Add more relevant keywords

    # Check if any of the health-related keywords are present in the reply
    for keyword in health_keywords:
        if keyword in reply.lower():
            return True
    return False

def chatbot_view(request):
    # user_profile = UserProfile.objects.get(user=request.user)
    conversation = request.session.get('conversation', [])

    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        prompts = []
        if user_input:
            conversation.append({"role": "user", "content": user_input})

        
        prompts.extend(conversation)

       
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompts,
            api_key="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",
        )

     
        chatbot_replies = [message['message']['content'] for message in response['choices'] if message['message']['role'] == 'assistant']

       
        health_advice_replies = []
        for reply in chatbot_replies:
            if is_health_related(reply):
                health_advice_replies.append(reply)

        # If no health-related advice is found, provide a friendly message
        if not health_advice_replies:
            health_advice_replies.append("I'm here to provide health-related advice, including topics like diet and nutrition. Feel free to ask any health-related questions.")

        greetings = ["hey", "hi", "hello","heyy"]
        if user_input.lower() in greetings:
            health_advice_replies.insert(0, "Hello! How can I assist you with your health-related questions today?")

        for reply in health_advice_replies:
            conversation.append({"role": "assistant", "content": reply})

        # Update the conversation in the session
        request.session['conversation'] = conversation
        

        return render(request, 'chatbot/chat.html', {'user_input': user_input, 'chatbot_replies': health_advice_replies, 'conversation': conversation})
    else:
        request.session.clear()
        return render(request, 'chatbot/chat.html', {'conversation': conversation})
