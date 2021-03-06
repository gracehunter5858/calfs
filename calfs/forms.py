
from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea, required=True)
