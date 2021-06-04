from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data["name"]) < 5:
            errors["name"] = "Please enter a valid name"
        if len(post_data["desc"]) < 15:
            errors["desc"] = "Please enter a valid description"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()