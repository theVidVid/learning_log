from django import forms

from .models import Topic


class TopicForm(forms.ModelForm):
    """Simple form for adding a topic"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
