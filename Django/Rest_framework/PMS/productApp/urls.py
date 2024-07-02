"""
URL configuration for PMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from productApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', views.getProductData),
    path('addProduct/', views.createProduct),
    path('updateProduct/<int:pk>', views.updateProduct),
    path('partialUpdateProduct/', views.partialUpdateProduct),
    path('deleteProduct/<int:id>/', views.delete_product),
    path('create/', views.addProductData.as_view(), name='create'),
    path('<int:pk>/', views.productDetailView.as_view(), name= 'detail'),
    path('listProducts/', views.productListView.as_view(), name='products'),
    path('update/<int:pk>/', views.productUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.productDeleteView.as_view(), name = 'delete')
]
