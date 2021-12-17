from django.urls import path
from . import views, resources

app_name = 'shop'

urlpatterns = [
    path('api/products', resources.get_products,
         name='product_list_api'),
    path('api/categories', resources.get_categories,
         name='categories_list_api'),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]
