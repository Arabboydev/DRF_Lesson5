from django.db import models
from django.contrib.auth.models import AbstractUser

ORDINARY_USER, ADMIN, MANAGER = ('ordinary_user', 'admin', 'manager')
VIA_EMAIL, VIA_PHONE = ('via_email', 'via_phone')
NEW, CONFIRM, DONE, DONE_PHOTO = ('new', 'confirm', 'done', 'done_type')


class Users(AbstractUser):
    USER_TYPES = (
        (ORDINARY_USER, ORDINARY_USER),
        (ADMIN, ADMIN),
        (MANAGER, MANAGER),
    )
    USER_VERIFICATION_TYPES = (
        (VIA_EMAIL, 'via_email'),
        (VIA_PHONE, 'via_phone'),
    )
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    user_role = models.CharField(max_length=50, choices=USER_TYPES, default=ORDINARY_USER)
    user_type = models.CharField(max_length=50, choices=USER_VERIFICATION_TYPES, default=NEW)
    user_status = models.CharField(max_length=20, default='active')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, blank=True, null=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username


class CodeVerify(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)
    time = models.DateTimeField(auto_now_add=True)
    user_type = models.CharField(max_length=50, choices=Users.USER_VERIFICATION_TYPES, default=VIA_EMAIL)

    class Meta:
        db_table = 'code_verify'

    def __str__(self):
        return self.user



