from django.shortcuts import render
from .forms import ProductAddForm, CategoryAddForm

def dashboard_index(request):
    return render(request, 'dashboard/dashboard.html')

def product_add(request):
    add_product=ProductAddForm()
    context={"form":add_product}
    return render(request, "products/product_add.html", context)

def product_index(request):
    return render(request, "products/product_index.html")

def product_edit(request):
    return render(request, "products/product_edit.html")

def product_view(request):
    return render(request, "products/product_view.html")


#categories
def category_add(request):
    add_category=CategoryAddForm()
    context={"form":add_category}
    return render(request, "products/product_add.html", context)