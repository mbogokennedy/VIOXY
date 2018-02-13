from django import forms
from crispy_forms.helper import FormHelper

class contactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-contorl', 'placeholder':'100 characters max'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-contorl', 'placeholder':'email@example.com'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class':'form-contorl', 'placeholder':'Comment Here Please'}))