from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Categoria(models.Model):
    name=models.CharField(max_length=50, default='1')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    imagen=models.ImageField(upload_to="blog/", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    date_posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='Anon')
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return '%s - %s' % (self.post.title, self.name)