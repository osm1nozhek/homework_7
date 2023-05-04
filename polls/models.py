from django.db import models



class Teacher(models.Model):
    name = models.CharField(max_length=200)
    subjects = models.CharField(max_length=200)

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Group(models.Model):
    name = models.CharField(max_length=100)
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student=models.ManyToManyField(Student, related_name='student_groups')









