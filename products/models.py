from django.db import models
from autoslug import AutoSlugField


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from="name", unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        to=Category,
        related_name="posts",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=255)
    overview = models.CharField(max_length=555)
    description = models.TextField()

    # arabic content
    ar_name = models.CharField(max_length=255, blank=True, null=True)
    ar_overview = models.CharField(max_length=555, blank=True, null=True)
    ar_description = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to="products/images/", blank=True, null=True)

    def __str__(self) :
        return str(self.id) + "--" + self.name
