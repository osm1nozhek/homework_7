import phonenumbers
from django import forms
from django.core.exceptions import ValidationError

from .models import Teacher, Group, Student


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["name", "subject"]


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "number"]

    def clean_number(self):
        phone_raw = self.cleaned_data["number"]
        try:
            phone=phonenumbers.parse(phone_raw,None)
        except phonenumbers.NumberParseException:
            raise ValidationError("Phone is invalid")
        if not phonenumbers.is_valid_number(phone):
            raise ValidationError("Phone is invalid")
        return phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name", "teacher", "student"]



