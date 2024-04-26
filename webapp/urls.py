from django.urls import path
from webapp.views import index, app_login, app_logout, professor_page, student_page

urlpatterns = [
    path('', index, name='app_index'),
    path('login/', app_login, name='app_login'),  
    path('logout/', app_logout, name='app_logout'),    
    path('student/', student_page, name='student_page'), 
    path('professor/', professor_page, name='professor_page')     
]