from django.db import models


# Create your models here.
class Comment(models.Model):
    name = models.CharField(blank=False, max_length=150)
    comment = models.TextField(blank=False, max_length=720)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
