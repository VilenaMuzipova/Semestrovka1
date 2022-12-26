from django.urls import path
from django.contrib import admin

from products import views

urlpatterns = [
    # path('', views.main, name='main'),
    # re_path(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
    path('product/<int:product_id>/', views.product, name='product'),
    #path('product/', views.product, name='product')
    #path('product/', views.product, name='product')
]

# from django.urls import path
# from products import views
#
# urlpatterns = [
#     # path('', views.home, name='ecomm-home'),
#     #path('products/', product.as_view()),
#     path('product/<int:product_id>/', views.product, name='product'),
# # ]
