from django.urls import path
from . import views

urlpatterns = [
    path("teacher/", views.add_teacher, name="add_teacher"),
    path(
        "teacher_edit_delete/<int:id>", views.teacher_edit_delete, name="teacher_change"
    ),
    path("teachers/", views.teacher_list, name="teacher_list"),
    path("student/", views.add_student, name="add_student"),
    path(
        "student_edit_delete/<int:id>", views.student_edit_delete, name="student_change"
    ),
    path("students/", views.student_list, name="student_list"),
    path("group/", views.add_group, name="add_group"),
]
