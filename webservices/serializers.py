from rest_framework import serializers
from webapp.models import Student, Professor, Course, Grade


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'professor']


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'


class StudentPersonalInfo(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone']


class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone']


class ProfessorPersonalInfo(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone']


class ProfessorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone']


