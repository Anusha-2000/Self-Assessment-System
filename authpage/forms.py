from django import forms
from .models import *
from .choices import *

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = {"fn", "ln", "email", "usr_nm", "roll_no", "sem_no", "branch"}
        widgets = {
            "fn": forms.TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'id': 'firstname',
                    'name': 'fname',
                    'placeholder': 'First Name',
                    'required': True
                }
            ), 
            "ln": forms.TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'id': 'lastName',
                    'name': 'lname',
                    'placeholder': 'Last Name',
                    'required': True
                }
            ), 
            "usr_nm": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'user',
                'name': 'usr_nm',
                'placeholder': 'Username',
                'required': True
            }),
            "email": forms.EmailInput(
                attrs={
                    'type': 'email',
                    'class': 'form-control',
                    'id': 'reg_email',
                    'name': 'email',
                    'placeholder': 'Your email',
                    'required': True
                }
            ),
            "roll_no": forms.TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'id': 'rn',
                    'name': 'rn',
                    'placeholder': 'Roll number',
                    'required': True
                }
            ),
            "sem_no": forms.NumberInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'id': 'sem_no',
                    'name': 'sem_no',
                    'placeholder': 'Semester number',
                    'maxlength': 1,
                    'required': True
                }
            ),
            "branch": forms.Select(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'id': 'branch',
                    'choices': Department,
                    'name': 'branch',
                    'required': True
                }
            )
        }