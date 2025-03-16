from django.forms import ModelForm, Textarea

from . import models

class CreateTodoForm(ModelForm):
    class Meta:
        model = models.TodoItem
        fields = ["title", "description"]
        widgets = {
            'description': Textarea(attrs={'cols': 30, 'rows': 5}),
        }
        