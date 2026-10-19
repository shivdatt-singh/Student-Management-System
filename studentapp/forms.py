
from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_number', 'email', 'age']

    
    def clean_roll_number(self):
        roll_number = self.cleaned_data['roll_number']

        existing_student = Student.objects.filter(
            roll_number=roll_number
        ).exclude(pk=self.instance.pk)

        if existing_student.exists():
            raise forms.ValidationError(
                "This roll number already exists. Please enter a unique roll number."
            )

        return roll_number
