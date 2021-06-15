from django.urls import path
from .views import home, products, customer
from . import views
urlpatterns = [
    path('signup/', views.registration, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('home/', views.home, name="home"),
    path('user/', views.userpage, name="user-page"),
    path('settings/', views.usersettings, name="settings"),
    path('customer/<int:pk>/', views.customer, name="customer"),
    path('products/', views.products, name="product"),
    path('create_order/', views.CreateOrder, name="create_order"),
    path('update_order/<int:pk>/', views.UpdateOrder, name="update_order"),
    path('delete_order/<int:pk>/', views.deleteorder, name="delete_order"),
]