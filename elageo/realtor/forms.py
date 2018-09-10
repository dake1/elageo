from django import forms
from .models import Property

# class FilterForm(forms.ModelForm):
#     PROPERTY_CHOICES = (
#         ('all','All'),
#         ('apartment','Apartment'),
#         ('house','House'),
#         ('office','Office'),
#         ('townhouse','Townhouse'),
#         ('warehouse','Warehouse'),
#         ('shop','Shop'),
#         ('land','Land')
#     )
#     property_type = forms.ChoiceField(choices=PROPERTY_CHOICES, widget=forms.Select(attrs={'placeholder': 'property type'}))
#     class Meta:
#         model = Property
#         fields = ('bed','bath','price')




class FilterForm(forms.Form):
    PROPERTY_CHOICES = (
        ('all','All'),
        ('apartment','Apartment'),
        ('house','House'),
        ('office','Office'),
        ('townhouse','Townhouse'),
        ('warehouse','Warehouse'),
        ('shop','Shop'),
        ('land','Land')
    )
    place = forms.CharField(required=False,  widget=forms.TextInput(attrs={'placeholder': 'place'}))
    property_type = forms.ChoiceField(required=False,choices=PROPERTY_CHOICES, widget=forms.Select(attrs={'placeholder': 'property type'}))
    bed  = forms.IntegerField(required=False,  widget=forms.NumberInput(attrs={'placeholder': 'number of beds'}))
    bath = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'placeholder': 'number of baths'}))
    price = forms.DecimalField( required=False, widget=forms.NumberInput(attrs={'placeholder': 'price less than'}))


class RequestViewingForm(forms.Form):
    name = forms.CharField(max_length=25,widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Phone'}))
    # comments = forms.CharField(required=False,widget=forms.Textarea(attrs={'placeholder': 'Comments'}))
