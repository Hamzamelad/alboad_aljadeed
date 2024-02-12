from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=555)
    overview= models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    img = models.ImageField(upload_to="blog/images/",blank=True, null=True)
    body = models.TextField()
