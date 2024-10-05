from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
    your_age = forms.CharField(label="Your Age", max_length=100)
