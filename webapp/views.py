from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from webapp.models import Course, Grade, Professor, Student


def index(request):
    user = request.user    

    if user.is_authenticated:                        
        username = request.user.username
        
        # Split the username by the dot (.)
        parts = username.split('.')
        
        # Check if the username follows the pattern username.role
        if len(parts) == 2:
            _, role = parts              
            
            role_pages = {
                'student': 'student_page',
                'professor': 'professor_page',                
            }            
            
            if role in role_pages:
                return redirect(role_pages[role])
        else:
            return HttpResponse(f"The user {username} doesn't have a Page.", status=404)
        
    else:
        return redirect('app_login')


def app_login(request):    
    request_method = request.method

    if request_method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)            
            return redirect('app_index')
      
    return render(request, 'webapp/login_page.html')


def app_logout(request):
    logout(request)
    return redirect('app_login')


def student_page(request):
    student = Student.objects.get(username=request.user.username)

    # Retrieve personal data
    personal_data = {
        'name': student.name,
        'email': student.email,
        'phone': student.phone
    }

    # Retrieve enrolled courses
    courses = student.courses.all()

    # Retrieve grades in courses
    grades = Grade.objects.filter(student=student)

    context = {
        'personal_data': personal_data,
        'courses': courses,
        'grades': grades
    }

    return render(request, 'webapp/student_page.html', context)


def professor_page(request):    
    professor = Professor.objects.get(username=request.user.username)

    # Retrieve personal data of the professor
    personal_data = {
        'name': professor.name,
        'email': professor.email,
        'phone': professor.phone
    }

    # Retrieve courses taught by the professor
    courses_taught = Course.objects.filter(professor=professor)

    # Retrieve grades assigned by the professor 
    grades_assigned = Grade.objects.filter(professor=professor)

    context = {
        'personal_data': personal_data,
        'courses_taught': courses_taught,
        'grades_assigned': grades_assigned,        
    }

    return render(request, 'webapp/professor_page.html', context)


