from django import forms  
from .models import project  
class projectForm(forms.ModelForm):  
    class Meta:  
        model = project  
        fields = "__all__"  