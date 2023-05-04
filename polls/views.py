from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render
from .forms import TeacherForm, StudentForm, GroupForm
from .models import Teacher, Student


def add_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse("teacher_change", args=[form.instance.id])
            )
    else:
        form = TeacherForm()
    return render(request, "teacher_form.html", {"form": form})


def teacher_edit_delete(request, id: int):
    try:
        teacher = Teacher.objects.get(id=id)
    except Teacher.DoesNotExist:
        return "Вчителя з таким індексом не існує"
    if request.method == "POST":
        if "edit" in request.POST:
            form = TeacherForm(request.POST, instance=teacher)
            if form.is_valid():
                form.save()
                return render(request, "teacher_edit_delete.html", {"form": form})
        else:
            teacher.delete()
            return HttpResponseRedirect(reverse("teacher_list"))
    else:
        form = TeacherForm(instance=teacher)
        return render(request, "teacher_edit_delete.html", {"form": form})


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teacher_list.html", {"teachers": teachers})


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse("student_change", args=[form.instance.id])
            )
    else:
        form = StudentForm()
    return render(request, "student_form.html", {"form": form})


def student_edit_delete(request, id: int):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return "Студента з таким індексом не існує"
    if request.method == "POST":
        if "edit" in request.POST:
            form = StudentForm(request.POST, instance=student)
            if form.is_valid():
                form.save()
                return render(request, "student_edit_delete.html", {"form": form})
        else:
            student.delete()
            return HttpResponseRedirect(reverse("student_list"))
    else:
        form = StudentForm(instance=student)
        return render(request, "student_edit_delete.html", {"form": form})


def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", {"students": students})


def add_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("add_group"))
    else:
        form = GroupForm()
        return render(request, "group_form.html", {"form": form})
