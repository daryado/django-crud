from django import forms
from UniversityApp.models import University, Student

class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['title', 'abbreviation', 'date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'abbreviation': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
               'placeholder': 'Select a date',
               'type': 'date'}),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'birthday', 'university', 'receipt_year']
        widgets = {
            'full_name': forms.TextInput(attrs={ 'class': 'form-control' }),
            'birthday': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
               'placeholder': 'Select a date',
               'type': 'date'
              }),
            'university': forms.TextInput(attrs={ 'class': 'form-control' }),
            'receipt_year': forms.TextInput(attrs={ 'class': 'form-control',
                                                    'placeholder': 'Select a year',
                                                    'type': 'number'}),
        }
