from django.urls import path
from webservices.views import StudentProfileView, StudentCoursesGradesView, ProfessorProfileView, ProfessorCoursesGradesView, ProfessorAssignGradesView

urlpatterns = [    
    path('student/profile/', StudentProfileView.as_view()),
    path('student/courses/', StudentCoursesGradesView.as_view()),
    path('professor/profile/', ProfessorProfileView.as_view()),
    path('professor/courses/', ProfessorCoursesGradesView.as_view()),
    path('professor/grades/<int:course_id>/<int:student_id>/', ProfessorAssignGradesView.as_view())
]
