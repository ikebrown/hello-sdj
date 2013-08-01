from django.db import models

class Hello(models.Model):
    email = models.EmailField()
    message = models.CharField(max_length=4000)
