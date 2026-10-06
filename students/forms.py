from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            'name',
            'email',
            'phone',
            'course',
        ]

        widgets = {

            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter full name'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter email'
                }
            ),

            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Enter phone number'
                }
            ),

            'course': forms.Select(),
        }