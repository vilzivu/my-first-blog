from django import forms
from django.utils import timezone
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        now_kiev = timezone.localtime(timezone.now())
        model = Post
        fields = ['author', 'pidrozdil', 'marshrut', 'sostav', 'data_viezd', 
                  'time_viezd', 'time_back']
        widgets = {
            'time_viezd': forms.TimeInput(format=now_kiev.strftime('%H:%M'), attrs={'type': 'time'}),
            'time_back': forms.TimeInput(format=now_kiev.strftime('%H:%M'), attrs={'type': 'time'}),
            'data_viezd': forms.DateInput(attrs={'type': 'date'})
        }


