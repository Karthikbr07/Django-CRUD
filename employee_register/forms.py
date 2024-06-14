from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):# we will desgin a form with required html file
    
    class Meta:
        model= Employee
        fields=('fullname','mobile','emp_code','position') # making all the properties of forms in models of Employee as field inside this form
        #or u can do this fields=('fullname','mobile',emp code','position') u can add or remove any fields based on your requirement
        #bu using fields='__all__' we can obtain all the fields
        labels={ # this is used to rename the fields/variables of the forms
            'fullname':'Full Name',
            'emp_code':'EMP code'
        }
        
    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label="Select" # making empty field as select in the dropdown
        self.fields['emp_code'].required=False # it indicates that emp_code in not neccesarily to be filled to submit the button
        
        