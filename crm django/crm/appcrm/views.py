from django.shortcuts import render
from .forms import Vshop, Vcustomer
from django.http import HttpResponse, HttpResponseRedirect
from .models import Customer, Shop


# Create your views here.

def home(request):
    u_name = "magesh"
    p_word = "1234"
    username = request.POST.get("user")
    password = request.POST.get("pswd")
    if username == u_name and password == p_word:
        return render(request, 'customer.html', {})
    return render(request, 'home.html', {})


def new_product(request):
    form = Vshop
    context = {'form': form}
    if request.method == 'POST':
        form = Vshop(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('product added successfully!')
    return render(request, 'product.html', context)


def check(request):
    if request.method == 'POST':
        n = request.POST.get('check')
        data = Shop.objects.filter(product=n)
        if data:
            return HttpResponseRedirect('/new_customer/')
        else:
            return HttpResponse('sorry,this product currently not available')
    return render(request, 'check.html', {})


def new_customer(request):
    form = Vcustomer
    context = {'form': form}
    if request.method == 'POST':
        form = Vcustomer(request.POST)
        print(request.POST)
        if form.is_valid():
            form.full_clean()
            form.save()
            return HttpResponse('order placed successfully!')
    return render(request, 'newcustomer.html', context)

def enquiry(request):
    if request.method == 'POST':
        s = request.POST.get('searchs')
        record = {"CustomerInfo": Customer.objects.all().filter(mobile=s)}
        return render(request, 'register.html', record)
    return render(request, 'search.html', {})


def update(request, id):
    info = Customer.objects.get(id=id)
    form = Vcustomer(instance=info)
    context = {"form": form, "info": info}
    if request.method == 'POST':
        form = Vcustomer(request.POST, instance=info)
        if form.is_valid():
            form.save()
            return HttpResponse("updated")
    return render(request, 'newcustomer.html', context)


def delete(request, id):
    obj = Customer.Objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect("/homepage/")

