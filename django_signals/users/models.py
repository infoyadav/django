from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.

class UserProfile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    mobile_no = models.CharField(verbose_name="User Cell Number", max_length=15)
    address = models.CharField(verbose_name = "User Address", max_length=250)
    dob = models.DateField(auto_now_add=True, verbose_name="User DOB")
    user_pic = models.ImageField(upload_to='user_profile/%Y-%m-%d/', height_field=None, width_field=None, max_length=None, validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])])
    
    def __str__(self):
        return self.staff
    
class Feedback(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user