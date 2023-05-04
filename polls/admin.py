from django.contrib import admin

from polls.models import Teacher, Group


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    ordering = ["name"]


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    ordering = ["name"]
