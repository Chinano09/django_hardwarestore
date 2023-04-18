from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import register, login_view

urlpatterns = [
    path('product_list', views.product_list, name='product_list'),
    path('create_product', views.create_product , name='create-product'),
    path('edit_product/<int:pk>', views.edit_product , name='edit-product'),
    path('delete_product/<int:pk>', views.delete_product , name='delete-product'),
    path('category_list', views.category_list , name='category-list'),
    path('create_category', views.create_category , name='create-category'),
    path('edit_category/<int:pk>', views.edit_category , name='edit-category'),
    path('delete_category/<int:pk>', views.delete_category , name='delete-category'),
    path('', views.home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', register, name='register'),
    path('product_list/<int:pk>/', views.category_products, name='category_products'),
]