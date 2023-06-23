from django.db import models

# Create your models here.

class Response(models.Model):
    # title = models.CharField(max_length=100)
    title = models.TextField(max_length=100)

    skills = models.CharField(max_length=200)
    tools = models.CharField(max_length=200)
    # Add any other fields you need
