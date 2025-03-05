from django import forms
from .models import Topic

class TopicForm(forms.model.Form):
    class meta:
        model = Topic
        fields = ['text']
        labels = {'text' : ''}