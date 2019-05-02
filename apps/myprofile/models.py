from django.db import models

# Create your models here.
class MyNote(models.Model):
    title = models.CharField(max_length=225)
    intro_info = models.TextField()
    categoty = models.CharField(max_length=225)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    udpated_at = models.DateTimeField(auto_now=True)
