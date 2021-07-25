#from django.djangoenv.pgportal.portal.models import Area, City
from django.shortcuts import render
from .models import City,Area, Pg, Sharing,Images
from django.http import JsonResponse
# Create your views here.
def index(request):
    cities=City.objects.all()
    return render(request,"PGPortal.html",{'cities':cities})
def json_area_response(request,*args, **kwargs):
    selected_city= kwargs.get('city_id')
    areas = list(Area.objects.filter(city_id=selected_city).values())
    print(areas)
    print(JsonResponse({'areas':areas}))
    return JsonResponse({'areas':areas})

def json_details_response(request,*args, **kwargs):
    print('in here')
    area_inp=kwargs.get('areas_id')
    print(area_inp)
    for_type_inp=int(kwargs.get('for_type'))
    food_inp=int(kwargs.get('food'))
    sharing_inp=int(kwargs.get('sharing'))
    price_range=int(kwargs.get('prince_range'))
    area_ids=list(Area.objects.filter(name=area_inp).values_list("id",flat=True))
    pg_ids=list(Pg.objects.filter(area_id__in=area_ids).values_list('id',flat=True))
    if for_type_inp!=3:
        pg_ids=list(Pg.objects.filter(id__in=pg_ids,pgtype=for_type_inp).values_list('id',flat=True))
    print("areas",area_ids)
    if food_inp!=3:
        pg_ids=list(Pg.objects.filter(id__in=pg_ids,food=food_inp).values_list('id',flat=True))
        print("in if")
    else:
        print('on else')
    if price_range>0:
        pg_ids=list(Sharing.objects.filter(pg_id__in=pg_ids,sharing_cap=sharing_inp,price__lte=price_range).values_list('pg_id',flat=True))
        pricing=list(Sharing.objects.filter(pg_id__in=pg_ids,sharing_cap=sharing_inp,price__lte=price_range).values())
    else:
        pg_ids=list(Sharing.objects.filter(pg_id__in=pg_ids,sharing_cap=sharing_inp).values_list('pg_id',flat=True))
        pricing=list(Sharing.objects.filter(pg_id__in=pg_ids,sharing_cap=sharing_inp).values())
    pg_return=list(Pg.objects.filter(id__in=pg_ids).values())
    print(pg_ids)
    print(pg_return)
    
    print(for_type_inp,food_inp,sharing_inp,area_inp,for_type_inp,price_range)
    print("pgs",pg_return)
    print("price",pricing)
    #return JsonResponse({'data': render('table.html','pg_details' == pg_return,'pg_pricing'==pricing)})
    return JsonResponse({"pg":pg_return,"price":pricing})

def images(request,*args, **kwargs):
    pg_id_inp=kwargs.get('pg_id')
    print(pg_id_inp)
    img=Images.objects.filter(pg_id=pg_id_inp).values()
    print(img)
    return render(request,'dispimages.html',{"img":img})
'''
def load_area(request):
    city_name=request.GET.get('city')
    areas=Area.objects.filter(City_id=city_name).order_by('name')
    return render(request,'dropdownlist.html',{'areas':areas})
'''