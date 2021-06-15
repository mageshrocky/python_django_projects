from django.urls import path
from .views import home, new_customer
from . import views

urlpatterns = [
    path('home/', home),
    path('check/', views.check, name='new'),
    path('new_product', views.new_product, name='add'),
    path('new_customer/', new_customer),
    path('enquiry/', views.enquiry, name='old'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name="delete")
]