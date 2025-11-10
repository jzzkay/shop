from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product
from .forms import ProductForm

# Create your views here.


def index(request, category_id = None):
    categories = Category.objects.all()
    if category_id:
        products = Product.objects.filter(category = category_id)
    else:
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

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app:index')
    else:
        form = ProductForm()
    return render(request, 'app/add_product.html', {'form': form})

def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('app:index')
    else:
        form = ProductForm(instance=product)
    return render(request, 'app/update_product.html', {'form': form})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('app:index')
    return render(request, 'app/delete_product.html', {'product': product})

