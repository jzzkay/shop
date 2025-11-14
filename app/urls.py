from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>', views.index, name='products_of_category'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('update/<int:product_id>/', views.update_product, name='update_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('order/<int:product_id>/', views.place_order, name='place_order'),
    path('order-success/', views.order_success, name='order_success'),
    path('comment/<int:product_id>/', views.add_comment, name='add_comment'),
]