from rest_framework.permissions import BasePermission

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        username = request.user.username        
        if username.endswith('.student'):
            return True
        
        else:        
            return False
        
class IsProfessor(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        username = request.user.username        
        if username.endswith('.professor'):
            return True
        
        else:        
            return False