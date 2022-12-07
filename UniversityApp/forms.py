from django import forms
from UniversityApp.models import University, Student


class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['university'].empty_label = "Select"

