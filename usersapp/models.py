# import datetime module to be used for dates and time manipulation
from datetime import date
import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = [
     ('Lecturer', ('Lecturer')),
     ('Student', ('Student'))
    ]

    DEPT_TYPE_CHOICES = [
     ('CIT', ('CIT')),
     ('EEE', ('EEE'))
    ]
    
    reg_no = models.CharField(max_length=20, verbose_name='Lecturer ID/Student ID')
    department = models.CharField(max_length=20, choices=DEPT_TYPE_CHOICES, null=False, blank=False)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, null=False, blank=False)
    gender = models.CharField(max_length=6, choices=[('Male', ('Male')), ('Female', ('Female'))], null=False, blank=False)
    phone = models.CharField(max_length=10, verbose_name="Phone Number", unique=True,
        help_text='The phone number should contain 10 digits e.g. 0881850090', null=False, blank=False)
    photo = models.ImageField(upload_to='media/users/',  null=True, blank=True)

    REQUIRED_FIELDS = ['reg_no', 'phone', 'email', 'first_name', 'last_name']

    # Helper function for checking if a person has an image or not
    @property
    def image_url(self):
        if self.person_photo and hasattr(self.person_photo, 'url'):
            return self.person_photo.url
        else:
            return 'images/icon/default_profile.png'

    def __str__(self):
        return self.email

    class Meta:
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ['reg_no', 'gender', 'last_name', 'first_name']
        get_latest_by =['date_joined', 'last_login']
        unique_together = ['reg_no', 'email']