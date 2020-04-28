from django import forms
from .models import Classified


class ClassifiedForm(forms.ModelForm):

    # image = forms.ImageField()

    class Meta:
        model = Classified
        fields = [
            'category', 'first_name', 'last_name', 'email', 'location', 'title', 'price', 'description', 'days_listed'
        ]
        labels = {
            'category': 'Category',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'location': 'Location',
            'title': 'Title',
            'price': 'Price',
            'description': 'Description',
            'days_listed': 'Days Listed'
        }
