from rest_framework import serializers

from apps.carts.models import CartItem

from ...models import Product


class ProductSerializer(serializers.ModelSerializer):
    is_selected = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "stock", "is_selected"]

    def get_is_selected(self, obj):
        user_email = self.context["request"].headers.get("X-User-Email")
        if user_email:
            return CartItem.objects.filter(user_email=user_email, product_id=obj.id).exists()
        return False
