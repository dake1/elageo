from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    subject=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    message=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
