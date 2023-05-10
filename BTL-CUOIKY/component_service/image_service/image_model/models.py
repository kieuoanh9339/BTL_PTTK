from django.db import models

# Create your models here.
class Image(models.Model):
    product_type_choices = (
        ('book', 'Book'),
        ('shoe', 'Shoe'),
        ('clothe', 'Clothe'),
        ('electronic', 'Electronic'),
    )
    
    product_type = models.CharField(choices=product_type_choices, max_length=50)
    product_id = models.IntegerField()
    image_url = models.URLField()
    
    def __str__(self):
        return f"{self.product_type} ({self.product_id}): {self.image_url}"