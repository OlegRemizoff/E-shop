from django import forms
from .models import Order



class OrderCreateForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = fields = ['first_name', 'last_name', 'email', 'city', 'address']
        widgets = {
            'first_name' : forms.TextInput(attrs={"class": "form-control"}),
            'last_name' : forms.TextInput(attrs={"class": "form-control"}),
            'email' : forms.EmailInput(attrs={"class": "form-control"}),
            'city' : forms.TextInput(attrs={"class": "form-control"}),
            'address' : forms.TextInput(attrs={"class": "form-control"}),
            'created' : forms.TextInput(attrs={"class": "form-control"}),
            'updated' : forms.TextInput(attrs={"class": "form-control"}),

        }


    # city 
    # address 
    # created 
    # updated 
    # paid 