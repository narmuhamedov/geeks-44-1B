from django.urls import path
from . import views

urlpatterns = [
    path('eat_food/', views.product_filter_view),
    path('product_electronic/', views.product_filter_view),
]