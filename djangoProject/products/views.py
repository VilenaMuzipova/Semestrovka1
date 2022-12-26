from django.shortcuts import render, get_object_or_404
from products.models import *
from products.forms import  CommentForm

def product(request, product_id):
    product = Product.objects.get(id=product_id)


    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)


    return render(request, 'products/product.html', locals())