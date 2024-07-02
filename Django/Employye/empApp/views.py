from django.shortcuts import render
from empApp.models import Employee
from empApp import forms

# Create your views here.
def empData(request):
    empdata = {'empNo' : 101, 'empName' : "Smith", "empSal" : 3000}
    empdata2 = {'empno' : 202, 'empname':"Saraswathi"}
    return render(request, 'emp.html', {'empdata' : empdata, 'empdata2': empdata2})

def empdb(request):
    data = Employee.objects.all()
    my_dict = {"empData" : data}
    # or directly give:
    # return render(request, 'emp.html', {'empData': Employee.objects.values()})
    return render(request, 'emp.html', context=my_dict)


def student(request):
    form = forms.Student()
    if request.method == 'POST':
        form = forms.Student(request.POST)
    if form.is_valid():
        print("Form is valid")
        print("Name : ", form.cleaned_data['name'])
        print('Age : ', form.cleaned_data['age'])
    return render(request, 'input.html', {'form' : form})