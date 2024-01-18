from django.db import models

class feed(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title