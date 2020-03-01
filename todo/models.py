from django.db import models

# Create your models here.

class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    complate = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text
    