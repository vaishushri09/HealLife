from django import forms
from .models import SleepPattern

class SleepPatternForm(forms.ModelForm):
    class Meta:
        model = SleepPattern
        fields = ['start_time', 'end_time', 'quality_rating']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


# posts/forms.py

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['prompt']
