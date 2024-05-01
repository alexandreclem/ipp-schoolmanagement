from django.urls import path
from webservices.views import StudentProfileView, StudentCoursesView, CourseGradesView, AverageGradesView

urlpatterns = [    
    path('student/profile/', StudentProfileView.as_view()),
    path('student/courses/', StudentCoursesView.as_view()),
    path('student/courses/<int:course_id>/grades/', CourseGradesView.as_view()),
    path('student/average_grades/', AverageGradesView.as_view()),
]
