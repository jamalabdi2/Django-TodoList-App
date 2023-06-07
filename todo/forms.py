from django.forms import ModelForm
from .models import TodoList
from django import forms

class TodoListForm(ModelForm):
    class Meta:
        model = TodoList
        fields = '__all__'

    def __init__(self, *args,**kwargs):
        is_editing = kwargs.pop('is_editing',False)
        super().__init__(*args,**kwargs)
        if not is_editing:
            self.fields['status'].widget = forms.HiddenInput()
            self.fields['status'].initial = TodoList.DEFAULT_STATUS
            self.fields['status'].required = False
    