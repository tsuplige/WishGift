from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    link = forms.URLField(required=False, label="Lien", widget=forms.URLInput(attrs={'placeholder': 'https://example.com'}))

    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'link']