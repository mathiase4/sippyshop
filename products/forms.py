from django import forms
from .models import Order, Review
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

class OrderForm(forms.ModelForm):
    """
    Form for collecting customer information at checkout.
    """
    country = CountryField(blank_label='(Select country)').formfield(
        widget=CountrySelectWidget(attrs={'class:': 'form-select'})
    )
    
    class Meta:
        model = Order
        fields = ['full_name', 'email', 'phone', 'address_line1', 'address_line2', 'city', 'postal_code', 'country']
        
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'address_line1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street Address 1'}),
            'address_line2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street Address 2'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postal Code'}),

        }
        # create form to make reviews.
class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        
        fields = ['rating', 'comment']