from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('products/product_details/<int:id>', views.details, name='details')
]
