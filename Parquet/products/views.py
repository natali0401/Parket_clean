from django.shortcuts import render,redirect
from .models import Massiv
from .models import Shpon
from .forms import OrderForm
from django.http import HttpResponse
from . import models
from django.utils.translation import gettext as _


def index (request):
    return render(request, "products/index.html")


def about (request):
    return render(request, "products/about.html")


def massiv (request):
    mas = Massiv.objects.all()
    return render(request, "products/massiv.html", {'mas':mas})


def contact (request):
    return render(request, "products/contact.html")


def shpon (request):
    shp = Shpon.objects.all()
    return render(request, "products/shpon.html", {'shp':shp})


def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form = models.Order.objects.create(**form.cleaned_data)
            return redirect('/')
        else:
            return HttpResponse(_('Invalid form'))
    else:
        form = OrderForm()
        context = {'form': form}
        return render(request, 'products/callback.html', context)


def callback(request):
    return render(request, 'products/callback.html')
