from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    students = models.ManyToManyField(Student, related_name='courses')

    def __str__(self):
        return self.title

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.name} - {self.course.title} - {self.date}"



class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    students = models.ManyToManyField(Student, related_name='courses')

    def __str__(self):
        return self.title
