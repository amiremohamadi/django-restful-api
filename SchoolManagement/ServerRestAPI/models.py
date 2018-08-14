from django.db import models


class Student(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    family = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Teacher(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    family = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Lecture(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class TeacherLecture(models.Model):
    TeacherID = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    LectureID = models.ForeignKey(Lecture, on_delete=models.CASCADE)


class StudentLecture(models.Model):
    StudentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    TeacherLectureID = models.ForeignKey(TeacherLecture, on_delete=models.CASCADE)