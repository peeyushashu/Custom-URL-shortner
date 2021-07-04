from django.db import models
# Create your models here.


class CustomURL(models.Model):
    slug = models.SlugField(unique=True)
    FullURL= models.URLField("URL", null=False)
    ShortURL= models.TextField()

    def __str__(self):
        return self.slug