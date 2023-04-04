from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path("dashboard/", views.dashboard_index, name='dashboard'),
    path("product/add/", views.product_add, name='product_add'),
    path("product/", views.product_index, name='product_index'),
    path("product/update/", views.product_update, name='product_update'),
    path("product/edit/<int:id>/", views.product_edit, name='product_edit'),
    path("product/view/<int:id>/", views.product_view, name='product_view'),
    path("product/delete/<int:id>/", views.product_delete, name='product_delete'),
    #categories
    path("category/add/", views.category_add, name='category_add')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)