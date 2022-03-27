from . models import Tas
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model=Tas
        fields=['name','priority','date']