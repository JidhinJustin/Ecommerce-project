from django.urls import path
from django.views.generic.base import RedirectView
from django.conf import settings
from django.contrib import admin
from . import views

urlpatterns = [
    path('login', views.loginadmin, name='login'),
    path('', RedirectView.as_view(url='login')),
    path('dashboard', views.admindashboard, name='admindashboard'),
    path('adminlogout', views.logoutadmin, name='adminlogout'),
    path('manageproducts', views.manageproducts, name='manageproducts'),
    path('add-product', views.addproduct, name='addproduct'),
    path('change-product-status', views.changestatus, name='changestatus'),
    path('edit-product/<int:product_id>', views.editproduct, name='editproduct'),
    path('delete-product/<int:product_id>', views.deleteproduct, name='deleteproduct'),
    path('manage-users', views.manageusers, name='manageusers'),
    path('change-user-status', views.changestatususer, name='changestatususer'),
    path('delete-user/<int:user_id>', views.deleteuser, name='deleteuser'),
    path('view-user/<int:user_id>', views.viewuser, name='viewuser'),
    path('admin-view-reports', views.adminviewreports, name='adminviewreports'),
    path('todayssalesreport', views.todayssalesreport, name='todayssalesreport'),
]