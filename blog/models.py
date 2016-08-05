from django.db import models
from django.utils import timezone

# Blog post model and object
class Post(models.Model):
    # Properties

    # Model field reference
    # https://docs.djangoproject.com/en/1.9/ref/models/fields/#field-types
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField() # Long text
    created_date = models.DateTimeField(default=timezone.now)
    publised_date = models.DateTimeField(blank=True, null=True)

    # Methods(Actions)
    def publish(self):
        self.publised_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    # prepare models for migration: ~/django_apps $ python manage.py makemigrations blog
    # create tables for models: ~/django_apps $ manage.py migrate blog
    # to edit and delete posts use Django admin blog/admin.py
