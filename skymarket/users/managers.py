from django.contrib.auth.models import (
    BaseUserManager
)


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone, password=None, role="user"):
        """ User creation function (user) - we pass the required fields to it. """

        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            is_admin=False,
            role=role,
            is_active=True,
        )

        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, phone, role="admin", password=None):
        """ Function for creating a superuser - with its help we create an administrator,
         this can be done using the createsuperuser command """

        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
            role=role,
        )

        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
