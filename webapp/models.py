from django.db import models


class Student(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True) 
    courses = models.ManyToManyField('Course', related_name='students')

    def __str__(self):
        return self.name


class Professor(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True) 

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    grade = models.FloatField()

    def __str__(self):
        return f"Grade for {self.student.name} in {self.course.name} assigned by {self.professor.name}: {self.grade}"
