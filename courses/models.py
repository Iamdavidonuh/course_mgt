from turtle import title
from django.db import models
from accounts.models import CustomUser

# Create your models here.


class Subject(models.Model):

    title = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title


class Course(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(
        CustomUser, related_name="course_by", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    students = models.ManyToManyField(
        CustomUser, related_name="courses_joined", blank=True
    )

    def __str__(self) -> str:
        return f"{self.title} by {self.teacher}"


class Module(models.Model):

    course = models.ForeignKey(Course, related_name="modules", on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    text = models.TextField(verbose_name="module_text")
    content = models.FileField(upload_to="videos/")

    def __str__(self) -> str:
        return self.title


class StudentCourseCompletion(models.Model):

    student = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)

    def __str__(self) -> str:
        return self.student
