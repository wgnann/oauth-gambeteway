from django.contrib.auth import get_user_model
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oauth.settings')
django.setup()

nusp = '6431176'
User = get_user_model()
user = User.objects.get(login=nusp)
user.is_staff = True
user.is_admin = True
user.is_superuser = True
user.save()
