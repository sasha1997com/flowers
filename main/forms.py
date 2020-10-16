from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=25)
    body = forms.CharField(required=False)