from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from jsonschema import ValidationError
from django.contrib.auth.models import User
from webapp.models import Professor, Student

# Post-save Students/Professors -> Creates and User instance related to them
@receiver(post_save, sender=Student)
def create_student_user(sender, instance, created, **kwargs):
    if created:
        User.objects.create_user(username=instance.username, email=instance.email, password='1234') # This default password is used only for TEST 

@receiver(post_save, sender=Professor)
def create_professor_user(sender, instance, created, **kwargs):
    if created:
        User.objects.create_user(username=instance.username, email=instance.email, password='1234') # This default password is used only for TEST 
# Post-delete Students/Professors -> Deletes the User instance related to them
@receiver(post_delete, sender=Student)
def delete_student_user(sender, instance, **kwargs):
    User.objects.filter(username=instance.username).delete()

@receiver(post_delete, sender=Professor)
def delete_professor_user(sender, instance, **kwargs):
    User.objects.filter(username=instance.username).delete()

# Pre-save Students/Professors -> Verify if the username follows the predefined pattern
def validate_username_pattern(sender, username):
    if sender == Student:
        if not username.endswith('.student'):
            raise ValidationError("Username must end with '.student'")
    elif sender == Professor:
        if not username.endswith('.professor'):
            raise ValidationError("Username must end with '.professor'")

@receiver(pre_save, sender=Student)
@receiver(pre_save, sender=Professor)
def validate_user(sender, instance, **kwargs):
    # Verify if the username already exists
    if User.objects.filter(username=instance.username).exists():
        raise ValidationError("Username already exists. Please choose a different one.")

    validate_username_pattern(sender, instance.username)

