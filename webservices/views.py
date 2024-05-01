from rest_framework.views import APIView
from rest_framework.response import Response
from webapp.models import Grade, Student, Professor
from webservices.serializers import StudentSerializer, CourseSerializer, GradeSerializer

# ~ Students APIs ~ #

# Show students personal information
class StudentProfileView(APIView):
    serializer_class = StudentSerializer    

    def get_object(self):
        return self.request.user.student

# Show students courses
class StudentCoursesView(APIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        return self.request.user.student.courses.all()

# Show students grades
class CourseGradesView(APIView):
    serializer_class = GradeSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return Grade.objects.filter(course_id=course_id, student=self.request.user.student)

# Show the average students scores in each course enrolled by them
class AverageGradesView(APIView):
    def get(self, request):
        student = self.request.user.student
        grades = Grade.objects.filter(student=student)
        total_grades = sum(grade.grade for grade in grades)
        if grades:
            average_grade = total_grades / len(grades)
        else:
            average_grade = 0
        return Response({'average_grade': average_grade})


# Professors APIs