from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)
    description = models.TextField(max_length=1024, unique=False, null=True)

    def __str__(self):
        return f'{self.name}'


class Course(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=64, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    teachers = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.name}'


class Lesson(models.Model):
    name = models.CharField(max_length=64)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Schedule(models.Model):
    date = models.DateTimeField(auto_now=False, null=False)
    lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.lesson}'

