from django.db import models


class CartItem(models.Model):
    """Cart item model"""

    user_email = models.EmailField()
    product_id = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"

    def __str__(self):
        return f"{self.user_email} - {self.product_id}"
