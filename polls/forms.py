from django import forms
from .models import Teacher, Group, Student


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["name", "subjects"]


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name"]


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields= ["name"]
