from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('product_list/', views.product_list, name='product_list'),
    path('product_list/product_details/<int:id>', views.details, name='details')
]
