from django import forms        #it will create form on the basis of model.
from .models import photo

class photoForm(forms.ModelForm): 

    class Meta:
        model = photo
        fields = ['title','record']
