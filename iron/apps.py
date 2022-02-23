from django.apps import AppConfig
from django.contrib.auth import get_user_model
import os
from sentry_sdk import capture_message


class IronConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'iron'

    @classmethod
    def ready(cls):
        try:
            user_model = get_user_model()
            django_su_email = os.environ.get('DJANGO_SU_EMAIL')
            django_su_password = os.environ.get('DJANGO_SU_PASSWORD')

            if not user_model.objects.filter(email=django_su_email).first():
                print("Creating superuser", django_su_email, django_su_password)
                user_model.objects.create_superuser(django_su_email, django_su_password)
        except Exception as e:
            capture_message(str(e))
            print("warning: super user can't be created yet")
