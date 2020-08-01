from django import forms
from django.forms import ModelForm
from .models import NewsStory


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'author', 'pub_date', 'image_url', 'content']
        css = {
            'all': ('styles.css')
        }
        widgets = {
            'pub_date': forms.DateInput(
                format=('%m/%d/%Y'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date',
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-text',  
                }
            )
        }