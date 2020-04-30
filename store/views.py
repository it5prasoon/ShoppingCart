from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Category, Product


# Create your views here.
def index(request):
    text_bar = 'A shopping Cart By Prasoon'
    return HttpResponse(text_bar)


def allProdcat(request, c_slug=None):
    c_page = None
    products = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products = Product.objects.filter(category=c_page, available=True)
    else:
        products = Product.objects.all().filter(available=True)
    return render(request, 'category.html', {'category': c_page, 'products': products})


def ProCatDetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': product})
