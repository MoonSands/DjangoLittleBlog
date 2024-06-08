from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
from pytils.translit import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.base import ContentFile
import requests
#from django_jsonfield import JSONField
from django_editorjs_fields import EditorJsJSONField


def upload_to(instance, filename):
    foldername = instance.__class__.__name__.lower()
    return '{foldername}/{filename}'.format(filename=filename,foldername=foldername)

class postContentFilesUpload(models.Model):
    file = models.FileField("/media/uploads/images/")


class post(models.Model):
    title = models.TextField(max_length=255)
    excerpt = models.TextField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    preview_image = models.ImageField(upload_to = upload_to, default='posts/moon.jpg')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True)
    category = models.ForeignKey('postCategory', on_delete=models.PROTECT, null=True)
    content = EditorJsJSONField()

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    #def get_absolute_url(self):
    #    return f"/posts/{self.slug}"

class postCategory(models.Model):
    name = models.TextField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(postCategory, self).save(*args, **kwargs)



#class postContent(models.Model):
#   post=models.ForeignKey('post', on_delete=models.PROTECT, null=True, related_name='content')
#   type_of_content = models.IntegerField(choices=CONTENT_TYPE_CHOICES)
#   content = models.TextField(blank=True, null=True)
#   order_num = models.IntegerField(default=0)
#   image = models.ImageField(upload_to='media/post', blank=True, null=True)
#   document = models.FileField(upload_to='media/docs', blank=True, null=True)
#
#   def __str__(self):
#       return f"Содержимое для поста {self.post.title}"
#
#    def save(self, *args, **kwargs):
#              response = requests.get(self.content, stream=True)
#              response.raise_for_status()  # Проверка на ошибки при запросе
#          file_name = self.content.split('/')[-1]  # Получаем имя файла из URL
#         if self.type_of_content == 2: 
#            self.image.save(file_name, ContentFile(response.content))
#       elif self.type_of_content == 3: 
#          self.document.save(file_name, ContentFile(response.content))    
#            except Exception as e:
#                print(f"Ошибка загрузки файла: {e}")
#                super(postContent, self).save(*args, **kwargs)
#        
                # В случае ошибки можно оставить поле content без изменения
        

#@receiver(post_save, sender=post)
#def create_post_content(sender, instance, created, **kwargs):
#    """
#    Создание записи PostContent при создании поста.
#    """
#    if created:
#        for content_item in instance.content:
#           postContent.objects.create(
#                post=instance,
#                type_of_content=content_item['type_of_content'],
#                content=content_item.get('content'),
#                order_num=content_item['order_num']
#            )

class docs(models.Model):
    name = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to = upload_to, default='docs/ИБ.docx')

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
       storage, path = self.file.storage, self.file.path
       super(docs, self).delete(*args, **kwargs)
       storage.delete(path)
    

class reportsGroup(models.Model):
    name = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    

class reports(models.Model):
    name = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to = upload_to, default='reports/%D0%98%D0%91_YdeVSTs.docx')
    group = models.ForeignKey('reportsGroup', on_delete= models.CASCADE , null=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
       storage, path = self.file.storage, self.file.path
       super(reports, self).delete(*args, **kwargs)
       storage.delete(path)

class faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question

class products(models.Model):
    name = models.TextField()
    preview_image = models.ImageField(upload_to = upload_to, default='products/moon.jpg')
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        storage, path = self.preview_image.storage, self.preview_image.path
        super(products, self).delete(*args, **kwargs)
        storage.delete(path)

class dataFromForms(models.Model):
    name = models.TextField(150, null=True)
    phone = models.IntegerField(11, null=True)
    email = models.TextField()
    message = models.TextField(null=True)

    def __str__(self):
        return self.email
        



