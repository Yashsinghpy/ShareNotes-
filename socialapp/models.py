from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class reg(models.Model):
          name=models.CharField(max_length=30)
          email=models.CharField(max_length=30)
          number=models.CharField(max_length=30)
          password=models.CharField(max_length=30)

class notes(models.Model):
          contents=models.CharField(max_length=30)
          user=models.ForeignKey(User, on_delete=models.CASCADE)
          date = models.DateTimeField(default=datetime.now)

class shared(models.Model):
          contents=models.CharField(max_length=30)
          recevier=models.CharField(max_length=30)
          sender=models.CharField(max_length=30)

