from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import OrderForm, CreateUserForm, CustomerForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group


# Create your views here.


@unauthenticated_user
def registration(request):
    # if request.user.is_authenticated:
    #    return redirect("/home")
    # else:
    form = CreateUserForm
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            #group = Group.objects.get(name='customer')
            #user.groups.add(group)
            #Customer.objects.create(user=user,name=user.username)
            return redirect("/login")
    context = {'form': form}
    return render(request, 'accounts/registration.html', context)


@unauthenticated_user
def loginPage(request):
    # if request.user.is_authenticated:
    #    return redirect("/home")
    # else:
    if request.method == "POST":
        u = request.POST.get("uname")
        p = request.POST.get("pswd")
        rec = authenticate(request, username=u, password=p)
        if rec is not None:
            login(request, rec)
            return redirect("/home")
    context = {}
    return render(request, 'accounts/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')


@login_required(login_url="/login")
#@allowed_users(allowed_roles=['admin'])
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    pending = orders.filter(status='Pending').count()
    context = {'orders': orders, 'customers': customers, 'total_customers': total_customers,
               'total_orders': total_orders, 'pending': pending}
    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url="/login")
@allowed_users(allowed_roles=['customer'])
def userpage(request):
    c = request.user.customer
    cust = Customer.objects.filter(name=c)
    orders = Order.objects.filter(customer__in=cust)
    context = {'cust': cust, 'orders': orders}
    return render(request, "accounts/user.html", context)


@login_required(login_url="/login")
@allowed_users(allowed_roles=['customer'])
def usersettings(request):
    c = request.user.customer
    form = CustomerForm(instance=c)
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=c)
        print(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("success")

    context = {"c": c, 'form': form}
    return render(request, "accounts/settings.html", context)


@login_required(login_url="/login")
def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/product.html', {'products': products})


@login_required(login_url="/login")
def customer(request, pk):
    cust = Customer.objects.filter(id=pk)
    orders = Order.objects.filter(customer__in=cust)
    myfilter = OrderFilter(request.GET, queryset=orders)
    orders = myfilter.qs
    context = {'cust': cust, 'orders': orders, 'myfilter': myfilter}
    return render(request, 'accounts/customer.html', context)


@login_required(login_url="/login")
def CreateOrder(request):
    form = OrderForm
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    context = {"form": form}
    return render(request, 'accounts/orderform.html', context)


@login_required(login_url="/login")
def UpdateOrder(request, pk):
    info = Order.objects.get(id=pk)
    form = OrderForm(instance=info)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=info)
        if form.is_valid():
            form.save()
            return redirect("/home")

    context = {'form': form, 'info': info}
    return render(request, 'accounts/orderform.html', context)


@login_required(login_url="/login")
def deleteorder(request, pk):
    info = Order.objects.get(id=pk)
    if request.method == "POST":
        info.delete()
        return redirect("/home")
    context = {'info': info}
    return render(request, 'accounts/delete.html', context)
