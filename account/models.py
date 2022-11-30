from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, number, password=None):
        """
        Creates and saves a User with the given number, date of
        birth and password.
        """
        if not number:
            raise ValueError('Users must have an number address')

        user = self.model(
            number=number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, number, password=None):
        """
        Creates and saves a superuser with the given number, date of
        birth and password.
        """
        user = self.create_user(
            number,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(verbose_name='نام کاربری', null = True, max_length=255)
    number = models.CharField(max_length=12 ,verbose_name="شماره تلفن")
    image = models.ImageField(upload_to='ImageUser/', null=True, blank=True)
    author = models.CharField(max_length=200)
    about_user = models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False, verbose_name='ادمین')

    objects = UserManager()

    USERNAME_FIELD = 'number'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربر ها'

    def get_absolute_url(self):
        return reverse("account:panel_user")

    def __str__(self):
        return self.number

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Otp(models.Model):
    token = models.CharField(max_length=200, null=True)
    number = models.CharField(max_length=11, verbose_name="شماره")
    code = models.SmallIntegerField(verbose_name="کد")
    expiration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.number


    class Meta:
        verbose_name_plural = "کدتاید"