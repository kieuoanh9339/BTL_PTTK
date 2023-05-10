
import uuid
from django.db import models
from user_model.models import user_registration
# from user_model.models import user_registration
# from user_model.models import user_registration
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.text import slugify

class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(user_registration, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    product = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f"{self.product} ({self.quantity})"

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.id))
        super(Cart, self).save(*args, **kwargs)

    @property
    def total_price(self):
        return self.quantity * self.price