"""
URL configuration for BookProject project.

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
from testApp.views import HelloWorldView, TemplateCBV, BookListView, BookCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hw/', HelloWorldView.as_view()),
    path('tw/', TemplateCBV.as_view()),
    path('booklist/', BookListView.as_view() ),
    path('create_book/', BookCreateView.as_view()),

]
