from django.http import HttpResponse
from django.shortcuts import render, redirect
from products.models import Products
from products.forms import Formulario_productos

def create_product(request):

    if request.method == 'POST':
        form = Formulario_productos(request.POST)

        if form.is_valid():
            Products.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                stock = form.cleaned_data['stock']
            )

            return redirect(list_products)

    elif request.method == 'GET':
        form = Formulario_productos()
        context = {'form':form}
        return render(request, 'products/new_product.html', context=context)

def list_products(request):
    products = Products.objects.all()
    context = {
        'products':products
    }
    return render(request, 'products/products_list.html', context=context)

def primer_formulario(request):
    print(request.method)
    if request.method == 'POST':
        Products.objects.create(name = request.POST ['name'])
    return render(request, 'products/primer_formulario.html', context={})

def search_products(request):
    search = request.GET['search']
    products = Products.objects.filter(name=search)
    print(products)
    return HttpResponse(request.GET)