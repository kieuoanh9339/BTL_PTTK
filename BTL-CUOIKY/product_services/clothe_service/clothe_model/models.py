from __future__ import unicode_literals
from django.db import models
from django.utils.text import slugify

class Clothe(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField() # số lượng tồn kho
    image = models.ImageField(upload_to='clothe_images/')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Clothe, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
