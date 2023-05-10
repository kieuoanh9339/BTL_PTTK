from django.db import models
from user_model.models import user_registration
from cart_model.models import Cart
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.CharField(max_length=200)
    billing_address = models.CharField(max_length=200)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"{self.user} - {self.date_created}"