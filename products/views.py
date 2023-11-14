from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Product


def products(request):
    product_list = Product.objects.all().values()
    context = {'product_list': product_list}
    template = loader.get_template('products.html')
    return HttpResponse(template.render(context, request))


def details(request, id):
    product = Product.objects.get(id=id)
    template = loader.get_template('product_details.html')
    context = {'product': product}
    return HttpResponse(template.render(context, request))


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
