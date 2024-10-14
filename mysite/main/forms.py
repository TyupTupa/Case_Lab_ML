from django import forms

class TextForm(forms.Form):
    text = forms.CharField(
        label='Введите отзыв на английском языке',
        widget=forms.Textarea(attrs={
            "class": "custom-textarea"  
        })
    )