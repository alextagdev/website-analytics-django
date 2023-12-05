# forms.py
from django import forms

class AnalysisForm(forms.Form):
    url = forms.URLField(
        label='Website URL',
        required=True,
        widget=forms.TextInput(attrs={'class': 'border p-2 w-full'})
    )
