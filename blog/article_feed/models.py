from django.db import models
from django.urls import reverse

def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)
def docs_upload_to(instance, filename):
    return 'docs/{filename}'.format(filename=filename)
def products_upload_to(instance, filename):
    return 'products/{filename}'.format(filename=filename)
    
class post(models.Model):
    title = models.TextField(max_length=255)
    #excerpt = models.TextField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    preview_image = models.ImageField(upload_to = upload_to, default='posts/moon.jpg')
    slug = models.SlugField(max_length=255, unique = True, db_index = True, verbose_name = 'URL')
    category = models.ForeignKey('postCategory', on_delete=models.PROTECT, null=False,default=1)

    def __str__(self):
        return self.title


class postCategory(models.Model):
    name = models.TextField(max_length=100)
    def __str__(self):
        return self.name

class postContent(models.Model):
    post=models.ForeignKey('post', on_delete=models.PROTECT, null=True, related_name='content')
    type_of_content = models.ForeignKey('postContentType', on_delete=models.PROTECT, null=True)
    content = models.TextField(null=True)
    order_num = models.IntegerField(null=True)

class postContentType(models.Model):
    type = models.TextField()
    def __str__(self):
        return self.type

class docs(models.Model):
    name = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=docs_upload_to, default='docs/test.pdf')
    type = models.ForeignKey('docsType', on_delete=models.PROTECT, null=True)

    def delete(self, *args, **kwargs):
       storage, path = self.file.storage, self.file.path
       super(docs, self).delete(*args, **kwargs)
       storage.delete(path)
    

class docsType(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class docsInPost(models.Model):
   doc = models.ForeignKey('docs', on_delete=models.PROTECT, null=True)
   post = models.ForeignKey('post', on_delete=models.PROTECT, null=True)  

class faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

class products(models.Model):
    name = models.TextField()
    preview_image = models.ImageField(upload_to = products_upload_to, default='products/moon.jpg')

    def delete(self, *args, **kwargs):
        storage, path = self.preview_image.storage, self.preview_image.path
        super(products, self).delete(*args, **kwargs)
        storage.delete(path)

class dataFromForms(models.Model):
    name = models.TextField(150)
    phone = models.IntegerField(11)
    email = models.TextField()
    message = models.TextField()



