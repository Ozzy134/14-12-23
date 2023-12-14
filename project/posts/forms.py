from django import forms

class AddState(forms.Form):
    title = forms.CharField(),
    text = forms.IntegerField(min_value=0),