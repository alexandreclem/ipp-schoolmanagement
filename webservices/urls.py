from django.urls import path
from webservices.views import StudentListCreateAPIView, ProfessorListCreateAPIView

urlpatterns = [
    path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('professors/', ProfessorListCreateAPIView.as_view(), name='professor-list-create'),
    # Add similar paths for courses and grades
]
