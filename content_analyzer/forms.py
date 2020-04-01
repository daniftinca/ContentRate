from django import forms


class AnalyzeForm(forms.Form):
    url_input = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL'}))
    target_query = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Target Query'}))
