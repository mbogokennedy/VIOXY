from django import forms

class additemForm(forms.Form):
    business_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-contorl', 'placeholder':'100 characters max'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-contorl', 'placeholder':'Describe your product here'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-contorl', 'placeholder':'email@example.com'}))
    contact = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-contro', 'placeholder':'0700000000'}))