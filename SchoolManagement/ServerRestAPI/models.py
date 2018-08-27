from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


# class MyUser(AbstractUser):
#     is_student = models.BooleanField(default=False)
#     is_teacher = models.BooleanField(default=False)


class Student(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20, default='1234')
    name = models.CharField(max_length=20)
    family = models.CharField(max_length=20)

    def __str__(self):
        return str(self.username)


class Teacher(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20, default='1234')
    name = models.CharField(max_length=20)
    family = models.CharField(max_length=20)

    def __str__(self):
        return str(self.username)


class Lecture(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class TeacherLecture(models.Model):
    TeacherID = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    LectureID = models.ForeignKey(Lecture, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{}_{}".format(self.TeacherID, self.LectureID)


class StudentLecture(models.Model):
    StudentID = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    TeacherLectureID = models.ForeignKey(TeacherLecture, on_delete=models.CASCADE, null=True)
    grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], default=0)

    def __str__(self):
        return "{}_{}".format(self.StudentID, self.TeacherLectureID)