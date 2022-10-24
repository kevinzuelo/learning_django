from django import forms
from app_Two.models import User

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = '__all__'