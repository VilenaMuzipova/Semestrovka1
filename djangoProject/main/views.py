from django.shortcuts import render
from main.forms import  SubscriberForm
from products.models import *

def main(request):
    name = "Top shop"
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print (data['name'])

        new_form= form.save()
    return render(request,'main/main.html', locals())

def home(request):
    products_images= ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones=products_images.filter(product__category__id=1)
    products_images_laptops=products_images.filter(product__category__id=2)
    products_images_smart=products_images.filter(product__category__id=3)
    return render(request,'main/home.html', locals())