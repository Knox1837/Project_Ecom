from django.urls import path
from . import views

urlpatterns=[
    path("dashboard/", views.dashboard_index, name='dashboard'),
    path("product/add/", views.product_add, name='product_add'),
    path("product/", views.product_index, name='product_index'),
    path("product/edit/", views.product_edit, name='product_edit'),
    path("product/view/", views.product_view, name='product_view'),

    #categories
    path("category/add/", views.category_add, name='category_add')
]