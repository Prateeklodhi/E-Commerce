from django.shortcuts import render
from pkg_resources import require

# Create your views here.
def store(request):
    context = {

    }
    return render(request,'store/store.html',context)


def cart(request):
    context = {

    }
    return render(request,'store/cart.html',context)


def checkout(request):
    context = {

    }
    return render(request,'store/checkout.html',context)