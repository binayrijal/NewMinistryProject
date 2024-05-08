import os
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db import models
from django.core.validators import RegexValidator
from datetime import date

class MyUserManager(BaseUserManager):
    def create_user(self, email, name, password=None,password2=None):
        """
        Creates and saves a User with the given email, date_of_birth,name,address,mobile_nmber and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            # address=address,
            # mobile_number=mobile_number

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        """
        Creates and saves a User with the given email, date_of_birth,name,address,mobile_nmber and password.
    
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            # address=address,
            # mobile_number=mobile_number
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    name=models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    updated_at=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



class Course(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    classnumber=models.IntegerField(null=False,blank=False)
    
    def __str__(self):
        return self.category
   

class Video(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='videos/')
 

    def filename(self):
        return os.path.basename(self.video_file.name)



class Timer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.IntegerField(default=0)