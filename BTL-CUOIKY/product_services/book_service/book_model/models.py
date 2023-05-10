from __future__ import unicode_literals
from django.db import models
from django.utils.text import slugify

class Book(models.Model):
    title = models.CharField(max_length=255) #tiêu đề sách
    slug = models.SlugField(unique=True, max_length=255, blank=True) #tạo đường link url lấy từng đối tượng sách
    author = models.CharField(max_length=255)  # tác giả
    publication_year = models.PositiveIntegerField() # Xuất bản năm nào
    description = models.TextField()  # mô tả
    price = models.DecimalField(max_digits=15, decimal_places=2) # giá sách
    inventory = models.PositiveIntegerField() # số lượng tồn kho
    image = models.ImageField(upload_to='book_images/')   # ảnh minh họa

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
