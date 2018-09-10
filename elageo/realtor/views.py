from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
# Create your views here.
from . models import Property
from . forms import FilterForm, RequestViewingForm



def rent_list(request):
    location_list = Property.objects.values('location').distinct()
    places = []
    for i in location_list:
        places.append(str(i['location']))

    places = sorted(places)
    current_page = 'rent_list'
    if request.method == 'POST':
        pass
        form = FilterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            fields = ('property_type','bed','bath','price')
            property_type = cd['property_type']
            bed = cd['bed']
            bath = cd['bath']
            price = cd['price']
            place = cd['place']

            if place == '':
                place = None

            if property_type == 'all' and place is None and bed is None and bath is None and price is None:
                return redirect('realtor:rent_list')
            else:
                filterquery = {}
                if place is not None:
                     filterquery.update(location=place)
                if property_type != 'all':
                    filterquery.update(property_type=property_type)
                if bed is not None:
                    filterquery.update(bed=bed)
                if  bath is not None:
                    filterquery.update(bath=bath)
                if price is not None:
                    filterquery.update(price__lte=price)
                filterquery.update(disposal_type='rent')
                rentals_list = Property.objects.filter(**filterquery).filter(available=True)
                # print(filterquery)
                # print("property_type: {} ,place:{}, bed:{},bath:{} ,price:{}".format(property_type,place,bed,bath,price))
                #------------paginator-----------------------------------------
                paginator = Paginator(rentals_list, 12) # 3 posts in each page
                page = request.GET.get('page')
                try:
                    rentals = paginator.page(page)
                except PageNotAnInteger:
                # If page is not an integer deliver the first page
                    rentals = paginator.page(1)
                except EmptyPage:
                # If page is out of range deliver last page of results
                    rentals = paginator.page(paginator.num_pages)


                return render(request,'realtor/list_rent.html',{'rentals':rentals,
                                                        'current_page':current_page,
                                                        'form':form,
                                                        'page':page,
                                                        'places':places,
        })

    else:
        form = FilterForm()
        rentals_list = Property.objects.filter(available=True,disposal_type='rent')
        #------------paginator-----------------------------------------
        paginator = Paginator(rentals_list, 12) # 3 posts in each page
        page = request.GET.get('page')
        try:
            rentals = paginator.page(page)
        except PageNotAnInteger:
        # If page is not an integer deliver the first page
            rentals = paginator.page(1)
        except EmptyPage:
        # If page is out of range deliver last page of results
            rentals = paginator.page(paginator.num_pages)

        return render(request,'realtor/list_rent.html',{'rentals':rentals,
                                                    'current_page':current_page,
                                                    'form':form,
                                                    'page':page,
                                                    'places':places,
    })

def rent_detail(request,id):
    prop = get_object_or_404(Property,id=id)
    num_pics=prop.pictures.all().count()
    num=range(num_pics)
    current_page = 'rent_list'
    if prop.lat and prop.long:
        cord = [prop.lat,prop.long]
    else:
        cord = None
    return render(request,'realtor/detail_rent.html',{'prop':prop,
                                                    'current_page':current_page,
                                                    'num':num,
                                                    'num_pics':num_pics,
                                                    'cord':cord,
    })


#----------------------------------SALE-------------------------------------------------------------------------------------



def sale_list(request):
    location_list = Property.objects.values('location').distinct()
    places = []
    for i in location_list:
        places.append(str(i['location']))

    places = sorted(places)
    current_page = 'sale_list'
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            fields = ('property_type','bed','bath','price')
            property_type = cd['property_type']
            bed = cd['bed']
            bath = cd['bath']
            price = cd['price']
            place = cd['place']


            if place == '':
                place = None

            if property_type == 'all' and place is None and bed is None and bath is None and price is None:
                return redirect('realtor:sale_list')
            else:
                filterquery = {}
                if place is not None:
                     filterquery.update(location=place)
                if property_type != 'all':
                    filterquery.update(property_type=property_type)
                if bed is not None:
                    filterquery.update(bed=bed)
                if  bath is not None:
                    filterquery.update(bath=bath)
                if price is not None:
                    filterquery.update(price__lte=price)
                filterquery.update(disposal_type='sale')
                sales_list = Property.objects.filter(**filterquery).filter(available=True)


                #------------paginator-----------------------------------------
                paginator = Paginator(sales_list, 12) # 3 posts in each page
                page = request.GET.get('page')
                try:
                    sales = paginator.page(page)
                except PageNotAnInteger:
                # If page is not an integer deliver the first page
                    sales = paginator.page(1)
                except EmptyPage:
                # If page is out of range deliver last page of results
                    sales = paginator.page(paginator.num_pages)

                return render(request,'realtor/list_sale.html',{'sales':sales,
                                                        'current_page':current_page,
                                                        'form':form,
                                                        'places':places,
        })

    else:
        form = FilterForm()
        sales_list = Property.objects.filter(available=True,disposal_type='sale')

        #------------paginator-----------------------------------------
        paginator = Paginator(sales_list, 12) # 3 posts in each page
        page = request.GET.get('page')
        try:
            sales = paginator.page(page)
        except PageNotAnInteger:
        # If page is not an integer deliver the first page
            sales = paginator.page(1)
        except EmptyPage:
        # If page is out of range deliver last page of results
            sales = paginator.page(paginator.num_pages)
        return render(request,'realtor/list_sale.html',{'sales':sales,
                                                    'current_page':current_page,
                                                    'form':form,
                                                    'places':places,
    })

def sale_detail(request,id):
    prop = get_object_or_404(Property,id=id)
    num_pics=prop.pictures.all().count()
    num=range(num_pics)
    current_page = 'sale_list'
    if prop.lat and prop.long:
        cord = [prop.lat,prop.long]
    else:
         cord = None
    return render(request,'realtor/detail_rent.html',{'prop':prop,
                                                    'current_page':current_page,
                                                    'num':num,
                                                    'num_pics':num_pics,
                                                    'cord':cord,
    })



def viewing_request(request, pid):
    prop = get_object_or_404(Property, id = pid)
    if request.method =='POST':
        form = RequestViewingForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = "viewing request from {} ({})".format( cd['name'], cd['email'])
            sender= cd['name']
            email = cd['email']
            phone = cd['phone']
            # comments = cd['comments']
            property_of_interest = request.build_absolute_uri(reverse('realtor:rent_detail', args=(prop.id, )))
            message = '{} \n phone:{} \n email:{} \n has sent a viewing request for {}.'.format(sender,phone,email, property_of_interest)
            send_mail(subject, message, email,['carlafenu@hotmail.com',])
            # messages.success(request,'Message sent successfully')
            return redirect(reverse('realtor:viewing_request_sent'))
            # return render(request,'realtor/viewing_request_sent.html',{})

    form = RequestViewingForm()
    return render(request,'realtor/viewing_request.html',{'form':form,
                                                        })

def viewing_request_sent(request):
    return render(request,'realtor/viewing_request_sent.html',{})
