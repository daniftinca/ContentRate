from django import forms


class AnalyzeForm(forms.Form):
    url_input = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

