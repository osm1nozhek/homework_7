from django.db import models




class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    subject=models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} {self.subject}"

class Group(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    group = models.ManyToManyField(Group)
    def __str__(self):
        return f"{self.first_name} {self.last_name}{self.group}"