from django.db import models


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} "


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Group(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return f"{self.name}"


class Result(models.Model):
    path = models.CharField(max_length=100)
    method = models.CharField(max_length=100)
    execution_time = models.FloatField(max_length=100)