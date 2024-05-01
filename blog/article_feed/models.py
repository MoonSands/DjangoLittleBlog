from django.db import models
from django.urls import reverse
class feed(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique = True, db_index = True, verbose_name = 'URL')
    category = models.ForeignKey('postCategory', on_delete=models.PROTECT, null=True)
    def get_absolute_url(self):
        return reverse('article', kwargs={'article_slug':self.slug})

class postCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

