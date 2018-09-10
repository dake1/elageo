from django.shortcuts import render
from realtor.models import Property

# Create your views here.

def home(request):
    current_page = 'home'
    rentals = Property.objects.filter(available=True,disposal_type='rent').order_by('-updated')[:3]
    sale = Property.objects.filter(available=True,disposal_type='sale').order_by('-updated')[:3]
    return render(request,'main/home.html',{'current_page':current_page,
                                            'rentals':rentals,
                                            'sale':sale,
    })

def services(request):
    current_page = 'services'
    return render(request, 'main/services.html',{'current_page':current_page,})

def aboutus(request):
    current_page = 'aboutus'
    return render(request,'main/aboutus.html',{'current_page':current_page,})
