from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img = models.ImageField()
    author = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.title
    

    def get_abolute_url(self):
        print(self.pk)
        return reverse('detail-article',kwargs = {'pk':self.pk})
