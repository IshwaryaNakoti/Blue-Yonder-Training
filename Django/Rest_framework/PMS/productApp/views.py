from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from rest_framework.decorators import api_view #class responsible to work with API
from rest_framework.response import Response
from .models import Product
from .serializer import ProductSerializer

# Create your views here.
@api_view(['GET'])
def getProductData(request):
    records = Product.objects.all()
    sdata = ProductSerializer(records, many = True)
    return Response(sdata.data)

@api_view(['POST'])
def createProduct(request):
    sdata = ProductSerializer(data = request.data)
    if sdata.is_valid():
        sdata.save() #Saving in the database
        return Response(sdata.data)
    else:
        return Response(sdata.errors)

@api_view(['PUT'])
def updateProduct(request, pk):
    #or you can say :  product = Product.objetcs.get(request.data['id'])
    product = get_object_or_404(Product, pk = pk)
    sdata = ProductSerializer(product, data = request.data)
    if sdata.is_valid():
        sdata.save()
        return Response(sdata.data)
    else:
        return Response(sdata.errors)

@api_view(['PATCH'])
def partialUpdateProduct(request):
    obj = Product.objects.get(id = request.data['id'])
    sdata = ProductSerializer(obj, data = request.data, partial = True)
    if sdata.is_valid():
        sdata.save()
        return Response(sdata.data)
    else:
        return Response(sdata.errors)

@api_view(['DELETE'])
def delete_product(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return Response({"status":"Record deleted"})
    
#class based insertion
class addProductData(CreateView):
    #Product_form.html
    model = Product
    fields = ('p_id', 'p_name', 'p_price')

class productDetailView(DetailView):
    #product_detail.html
    model = Product

class productListView(ListView):
    #product_list.html
    model = Product

class productUpdateView(UpdateView):
    model = Product
    fields = ('p_id', 'p_name', 'p_price')
    success_url = reverse_lazy('products')

class productDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products')






