from django import forms
from .models import Teacher, Group, Student


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["name","group"]


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name","group"]


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields= ["name"]

class AddStudentToGroupForm(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.all())