from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    priority_level=models.IntegerField()
    creation_time=models.DateTimeField(auto_now_add=True,null=True)