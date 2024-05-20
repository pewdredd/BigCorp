from django.shortcuts import render, get_object_or_404

from .models import ProductProxy, Category

def products_view(request):
    products = ProductProxy.objects.all()
    return render(request, 'shop/products.html', products)

def products_detail_view(request, slug):
    product = get_object_or_404(ProductProxy, slug)
    return render(request, 'shop/products_detail.html', product)

def category_list_view(request, slug):
    category = get_object_or_404(Category, slug)
    products = ProductProxy.objects.select_related('category').all()
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'shop/category_list.html', context)

