from rest_framework.views import APIView, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from webservices.permissions import IsStudent, IsProfessor

from webapp.models import Student, Professor, Course, Grade
from webservices.serializers import StudentPersonalInfo, StudentUpdateSerializer, ProfessorPersonalInfo, ProfessorUpdateSerializer


# ~ Students APIs ~ #

# Students personal information
class StudentProfileView(APIView): 
    '''Students personal information'''  

    authentication_classes = [SessionAuthentication]  
    permission_classes = [IsAuthenticated, IsStudent]        

    def get(self, request):
        student = Student.objects.filter(username=request.user.username)
        serializer = StudentPersonalInfo(student, many=True)
        return Response(serializer.data)
    
    def put(self, request):
        student_id = Student.objects.filter(username=request.user.username).values_list('id', flat=True).first()
        student = get_object_or_404(Student, id=student_id)
        serializer = StudentUpdateSerializer(student, data=request.data, partial=True)  

        if serializer.is_valid():            
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Student Courses and Grades
class StudentCoursesGradesView(APIView):  
    '''Student Courses and Grades'''  

    authentication_classes = [SessionAuthentication]  
    permission_classes = [IsAuthenticated, IsStudent]

    def get(self, request):        
        student = Student.objects.filter(username=request.user.username).first()
        courses_of_student = student.courses.all()
        
        data = []
        for course in courses_of_student:
            grades = Grade.objects.filter(student=student, course=course)
            grade_values = [grade.grade for grade in grades]

            course_data = {
                "name": course.name,
                "professor": course.professor.name,
                "grades": grade_values
            }
            data.append(course_data)

        return Response(data)
    

# ~ Professor APIs ~ #

# Pofessor personal information
class ProfessorProfileView(APIView): 
    '''Pofessor Personal Information'''   

    authentication_classes = [SessionAuthentication]  
    permission_classes = [IsAuthenticated, IsProfessor]        

    def get(self, request):
        professor = Professor.objects.filter(username=request.user.username)
        serializer = ProfessorPersonalInfo(professor, many=True)
        return Response(serializer.data)
    
    def put(self, request):
        professor_id = Professor.objects.filter(username=request.user.username).values_list('id', flat=True).first()
        professor = get_object_or_404(Professor, id=professor_id)
        serializer = ProfessorUpdateSerializer(professor, data=request.data, partial=True)  

        if serializer.is_valid():            
            serializer.save()
            return Response(serializer.data)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Professor Courses and Grades
class ProfessorCoursesGradesView(APIView):  
    '''Professor Courses and Grades'''

    authentication_classes = [SessionAuthentication]  
    permission_classes = [IsAuthenticated, IsProfessor]

    def get(self, request):                       
        professor = Professor.objects.get(username=request.user.username)
        courses_of_professor = Course.objects.filter(professor=professor)

        data = []
        for course in courses_of_professor:
            students_with_grades = []
            for student in course.students.all():
                grades_list = [grade.grade for grade in Grade.objects.filter(student=student, course=course, professor=professor)]
                students_with_grades.append({
                    "course_id": course.id,
                    "student_id": student.id,
                    "student_name": student.name,
                    "grades": grades_list
                })
            data.append({course.name: students_with_grades})

        return Response(data)


# Professor assign Grades
class ProfessorAssignGradesView(APIView):
    authentication_classes = [SessionAuthentication]  
    permission_classes = [IsAuthenticated, IsProfessor]

    def get_user_objects(self, request, course_id, student_id):
        professor = get_object_or_404(Professor, username=request.user.username)
        course = get_object_or_404(Course, id=course_id)
        student = get_object_or_404(Student, id=student_id)
        return professor, course, student

    def get(self, request, course_id, student_id):
        professor, course, student = self.get_user_objects(request, course_id, student_id)
        grades = Grade.objects.filter(student=student, course=course, professor=professor)
        grades_list = [grade.grade for grade in grades]
        data = [{
            'course_name': course.name,
            'student_name': student.name,
            'grades': grades_list
        }]
        return Response(data)

    def post(self, request, course_id, student_id):
        professor, course, student = self.get_user_objects(request, course_id, student_id)
        grade_value = request.data.get('grade')
        if grade_value is None:
            return Response({"error": "Please provide 'grade' field in the request data"}, status=status.HTTP_400_BAD_REQUEST)
        
        Grade.objects.create(professor=professor, student=student, course=course, grade=grade_value)
        return Response({"success": f"Grade {grade_value} assigned to student {student.name} in course {course.name}"}, status=status.HTTP_200_OK)

    def delete(self, request, course_id, student_id):
        professor, course, student = self.get_user_objects(request, course_id, student_id)
        num_deleted, _ = Grade.objects.filter(course=course, professor=professor, student=student).delete()
        return Response({"success": f"Deleted {num_deleted} grades for student {student.name} in course {course.name}"}, status=status.HTTP_200_OK)