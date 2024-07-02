from django.shortcuts import render
from ProductApp import forms

# Create your views here.
def product_details(request):
    form = forms.ProductForm()
    if request.method == 'POST' :
        form = forms.ProductForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            print("P_id : ", form.cleaned_data['p_id'])
            print("P_Name : ", form.cleaned_data['p_name'])
            print("P_price : ", form.cleaned_data['p_price'])
            form.save()
    return render(request, 'input.html', {'form' : form})

def template_inheritance_parent(request):
    d = {'name' : "Ishwarya"}
    return render(request, 'base.html', context=d)

def template_inheritance_child(request):
    return render(request, 'child.html')