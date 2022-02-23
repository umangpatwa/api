from django.db.models import Model, UUIDField, CharField, DateTimeField, TextField, EmailField, JSONField
from django.utils.translation import ugettext_lazy as _
# from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# from datetime import datetime
# import uuid
# import arrow


# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         if email is None:
#             raise TypeError('Users must have an email address.')
#
#         user = self.model(email=self.normalize_email(email))
#         user.set_password(password)
#         user.save(using=self._db)
#
#         return user
#
#     def create_superuser(self, email, password=None):
#         if password is None:
#             raise TypeError('Superusers must have a password.')
#
#         user = self.create_user(email, password)
#         user.is_superuser = True
#         user.is_admin = True
#         user.is_staff = True
#         user.save(using=self._db)
#
#         return user
#

# class User(AbstractUser):
#     # username = TextField(blank=True, null=True)
#     username = None
#     # groups = ForeignKey(Group, on_delete=CASCADE)
#     email = EmailField(_('email address'), unique=True,max_length=255,)
#
#     USERNAME_FIELD = 'email'
#
#     is_active = BooleanField(default=True)
#     is_admin = BooleanField(default=False)
#     objects = CustomUserManager()
#     # REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
#     REQUIRED_FIELDS = []
#
#     def __str__(self):
#         return "{}".format(self.email)
# class UserProfile(Model):
#     user = OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name='profile')
#     title = CharField(max_length=5)
#     dob = DateField()
#     address = CharField(max_length=255)
#     country = CharField(max_length=50)
#     city = CharField(max_length=50)
#     zip = CharField(max_length=5)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False, is_active=True, is_superuser=False):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )
        # user.full_name = full_name
        user.set_password(password)  # change password to hash
        # user.profile_picture = profile_picture
        # user.gender = gender
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.is_active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            # full_name,
            # profile_picture,
            # gender,
            password=password,
            is_staff=True,
            is_active=True,
            is_superuser=True
        )
        return user


class User(AbstractUser):
    """User model."""

    username = None
    email = EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
