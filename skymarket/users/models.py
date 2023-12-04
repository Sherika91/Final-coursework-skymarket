from django.contrib.auth.models import AbstractUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _

NULLABLE = {'null': True, 'blank': True}


class UserRoles:
    USER = 'user'
    ADMIN = 'admin'

    CHOICES = (
        (USER, _('user')),
        (ADMIN, _('admin')),
    )


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email', validators=[EmailValidator])

    first_name = models.CharField(max_length=35, verbose_name='First Name', **NULLABLE, )
    last_name = models.CharField(max_length=35, verbose_name='Last Name', **NULLABLE, )
    phone = PhoneNumberField(max_length=35, verbose_name='Phone', **NULLABLE, region='RU', )
    role = models.CharField(choices=UserRoles.CHOICES, default=UserRoles.USER, max_length=10, verbose_name='Role')
    image = models.ImageField(upload_to='images/', verbose_name='Avatar', **NULLABLE, )

    is_active = models.BooleanField(default=True, verbose_name='Active Status', )
    is_admin = models.BooleanField(default=False, verbose_name='Admin Status', )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']

    objects = UserManager()

    def __int__(self):
        return f"{self.email}"

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    @is_admin.setter
    def is_admin(self, value):
        self.role = UserRoles.ADMIN if value else UserRoles.USER

    @is_user.setter
    def is_user(self, value):
        self.role = UserRoles.USER if value else UserRoles.ADMIN

    @is_superuser.setter
    def is_superuser(self, value):
        self.is_admin = value

    @is_staff.setter
    def is_staff(self, value):
        self.is_admin = value

    class Meta:
        ordering = ('-id',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'
