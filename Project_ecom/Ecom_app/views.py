from django.shortcuts import render, redirect
from .forms import ProductAddForm, CategoryAddForm
from .models import Category, Product
from django.contrib.auth.models import User

def dashboard_index(request):
    return render(request, 'dashboard/dashboard.html')


#Products
def product_add(request):
    add_product=ProductAddForm()
    context={"form":add_product}

    if request.method=='POST':
        category=Category.objects.get(id=request.POST.get('category'))

        user= User.objects.get(username='knox')
        product=Product()
        product.title=request.POST.get('title')
        product.desc=request.POST.get('desc') 
        product.price=request.POST.get('price')
        product.quantity=request.POST.get('quantity')
        product.discount=request.POST.get('discount')
        product.cash_on_delivery=request.POST.get('cash_on_delivery')
        product.category=category
        product.user=user
        product.save()
        return redirect('product_index')


    return render(request, "products/product_add.html", context)

def product_index(request):
    products= Product.objects.all()
    context={'data': products}
    return render(request, "products/product_index.html", context)

def product_edit(request, id):
    product=Product.objects.get(id=id)
    context={'data':product}
    return render(request, "products/product_edit.html", context)

def product_view(request, id):
    product=Product.objects.get(id=id)
    context={'data':product}
    return render(request, "products/product_view.html", context)

def product_delete(request, id):
    product=Product.objects.get(id=id)
    product.delete()
    return redirect(product_index)



#categories
def category_add(request):
    add_category=CategoryAddForm()
    context={"form":add_category}

    if request.method=='POST':
        catgry= Category()
        catgry.category_name=request.POST.get('category_name')
        catgry.save()

    return render(request, "categories/add_category.html", context)