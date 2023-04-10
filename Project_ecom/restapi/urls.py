from django.urls import path
from .views import CategoryApiView, ProductApiView, ProductApiIdView, LoginApiView, RegisterApiView
urlpatterns=[
    path('category/', CategoryApiView.as_view(), name='category'),
    path('product/', ProductApiView.as_view(), name='product'),
    path('product/<int:id>/', ProductApiIdView.as_view(), name='product-viewbyid'),
    path('product/login/', LoginApiView.as_view(), name='loginapi'),
    path('product/register/', RegisterApiView.as_view(), name='registerapi'),
]