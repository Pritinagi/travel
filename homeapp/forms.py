from django import forms
from .models import contact

class ContactForm(forms.Form):
    class Meta:
        model=contact
    