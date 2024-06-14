from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
# Create your views here.

def employee_list(request):
    context={'employee_list':Employee.objects.all()}
    return render(request,"employee_register/employee_list.html",context)

def employee_form(request,id=0): #id is mentioned incase of an update, if no id number is given it's default value will be taken( i.e 0)
    if request.method == "GET":
        if id==0:
            form=EmployeeForm() #creating the object form and assigning the instance of employee form
        else:
            employee=Employee.objects.get(pk=id)
            form=EmployeeForm(instance=employee)
        return render(request,"employee_register/employee_form.html",{'form':form}) 
    else:
        if id==0:
            form=EmployeeForm(request.POST)
        else:
            employee=Employee.objects.get(pk=id)
            form=EmployeeForm(request.POST,instance=employee)
            
        if form.is_valid():
            form.save()
        return redirect("/employee/list")   
            
def employee_delete(request,id):
    employee=Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')