from django.urls import path, include
from .import views
from .views import index, ViewProduct, CategoryView

urlpatterns = [
    path('', index, name='index'),
    path('market/category/<str:slug>', ViewProduct.as_view(), name='product'),
    path('category/<str:slug>', CategoryView.as_view(), name='category'),
]