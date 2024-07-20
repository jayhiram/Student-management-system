from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course, Attendance
from .forms import StudentForm, CourseForm, AttendanceForm
from django.views.decorators.csrf import csrf_protect

def index(request):
    return render(request, 'students/index.html')

def list_students(request):
    students = Student.objects.all()
    return render(request, 'students/list_students.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})

def list_courses(request):
    courses = Course.objects.all()
    return render(request, 'students/list_courses.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_courses')
    else:
        form = CourseForm()
    return render(request, 'students/add_course.html', {'form': form})

def mark_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_attendance')
    else:
        form = AttendanceForm()
    return render(request, 'students/mark_attendance.html', {'form': form})

def list_attendance(request):
    attendance_records = Attendance.objects.all()
    return render(request, 'students/list_attendance.html', {'attendance_records': attendance_records})

@csrf_protect
def student_form_view(request):
    if request.method == "POST":
        # Handle form submission
        pass
    return render(request, 'student_form.html')