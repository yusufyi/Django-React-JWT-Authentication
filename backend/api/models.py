from django.db import models
from django.contrib.auth.models import User
from sqlalchemy import null

# Create your models here.

class Note(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    note = models.TextField()