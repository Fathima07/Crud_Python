from cProfile import label
from .models import Employee
from django import forms




class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname','emp_code','mobile','position')
        label = {
            'fullname' :'Full Name',
            'emp_code' :'EMP.Code'
        }
    
    def __init__(self,*args,**kwargs):  #to add the "select" option into dropdown list
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False