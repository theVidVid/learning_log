from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """Simple form for adding a topic"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(form.ModelForm):
    """Simple form for adding an entry."""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
