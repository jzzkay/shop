from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.


def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories' : categories,
        'products' : products
    }
    return render(request, 'app/home.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()

    context = {
        'product': product,
        'categories': categories
    }
    return render(request, 'app/product_detail.html', context)
