from django.contrib import admin
from .models import Post

admin.site.register(Post)

# to log in create a superuser $ python manage.py createsuperuser
