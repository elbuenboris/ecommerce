from django.shortcuts import render
from products.models import Products


def create_product(request):
    productos =Products.objects.all
    context = {}
    if len(productos) >= 3:
        new_product = Products.objects.create(name = 'Coca cola 1lt', price = 20, stock = 10)
        context = {
            'new_product':new_product
    }
    return render(request, 'products/new_product.html', context=context)

def list_products(request):
    products = Products.objects.all()
    context = {
        'products':products
    }
    return render(request, 'products/products_list.html', context=context)

def primer_formulario(request):
    return render(request, 'products/primer_formulario.html', context={})