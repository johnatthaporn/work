from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import Items, UserCart
# Create your views here.
def choose(request):
    return render(request, 'work/choose.html')

def sell(request):
    return render(request, 'work/sell.html')

def buy(request):
    context = {'items':Items.objects.all()}
    return render(request, 'work/buy.html', context)

def item(request, pk):
    context = {'item':Items.objects.get(pk=pk)}
    return render(request, 'work/item.html', context)

def cart_item(request, pk):
    context = {'item':Items.objects.get(pk=pk)}
    return render(request, 'work/cart_item.html', context)


@login_required
def before_cart(request, pk):
    choose_item = Items.objects.get(pk=pk)
    x = UserCart(buyer=request.user, item=choose_item)
    x.save()
    return HttpResponseRedirect(reverse('work:cart'))

@login_required
def cart(request):
    context = {'items':UserCart.objects.filter(buyer=request.user)}
    return render(request, 'work/cart.html', context)
@login_required
def add_item(request):
    if request.method == "POST":
        name = request.POST['name']
        picture = request.FILES['picture']
        description = request.POST['description']
        x = Items(name=name, picture=picture, description=description, ownby=request.user)
        x.save()
        return HttpResponseRedirect(reverse('work:buy'))

    else:
        return render(request, 'work/add_item.html')