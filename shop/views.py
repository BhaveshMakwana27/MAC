from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Order,OrderUpdate
from math import ceil
import json
# Create your views here.
def index(request):
    
    allProds = []
    catProds = Product.objects.values('category','id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prods = Product.objects.filter(category=cat)
        n = len(prods)
        nSlides = n//4 + ceil(n/4 - n//4)
        allProds.append([prods,nSlides,range(1,nSlides)])
    params = {'allProds':allProds}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def searchMatch(query,item):
    q = query.lower()
    if q in item.desc.lower() or q in item.product_name.lower() or q in item.category.lower() or q in item.subcategory.lower():
        return True
    return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catProds = Product.objects.values('category','id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prodTemp = Product.objects.filter(category=cat)
        prod = [item for item in prodTemp if searchMatch(query,item)]
        n = len(prod)
        nSlides = n//4 + ceil(n/4 - n//4)
        if(len(prod)!=0):
            allProds.append([prod,nSlides,range(1,nSlides)])
    params = {'allProds':allProds}
    if (len(allProds) == 0 or len(query)<1):
        params={'msg':'Prease make sure to enter relevant query....'}
    return render(request,'shop/search.html',params)

def contactUs(request):
    if(request.method == 'POST'):
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phoneNo = request.POST.get('phoneNo','')
        query =request.POST.get('query','')

        qDetail = Contact(name=name,email=email,phoneNo=phoneNo,query=query)
        qDetail.save()
        return render(request,'shop/contact.html',{'contact_status':True})

    return render(request,'shop/contact.html',{'contact_status':True})

def prodView(request,myid):
    product = Product.objects.filter(id=myid)
    return render(request,'shop/prodView.html',{'product':product[0]})


def tracker(request):
    if(request.method == 'POST'):
        orderId = request.POST.get('orderid','')
        email = request.POST.get('email','')
        try:
            order = Order.objects.filter(order_id=orderId,email=email)
            if(len(order)>0):
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates=[]
                for i in update:
                    updates.append({'text':i.update_desc,'time':i.timestamp})
                    response = json.dumps([updates,order[0].items_json],default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
        
    return render(request,'shop/tracker.html')

def checkout(request):
    if(request.method == 'POST'):
        items_json = request.POST.get('itemJson','')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('address','')
        phoneNo = request.POST.get('phoneNo','')
        city =request.POST.get('city','')
        state =request.POST.get('state','')
        zip_code =request.POST.get('zip','')

        order_details = Order(items_json=items_json,name=name,email=email,phoneNo=phoneNo,address=address,city=city,state=state,zip_code=zip_code)
        order_details.save()
        order_update = OrderUpdate(order_id=order_details.order_id, update_desc='Your order is in process now...')
        order_update.save()
        thank = True
        id = order_details.order_id
        return render(request,'shop/checkout.html',{'thank':thank,'id':id})

    return render(request,'shop/checkout.html')


def viewCart(request):
    allProds = Product.objects.values('image')

    return render(request,'shop/cart.html',{'allProds':allProds})