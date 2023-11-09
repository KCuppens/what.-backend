from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from ...models import CartItem
from .serializers import CartItemSerializer


class ToggleCartItemView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            user_email = serializer.validated_data["user_email"]
            product_id = serializer.validated_data["product_id"]

            cart_item, created = CartItem.objects.get_or_create(
                user_email=user_email, product_id=product_id
            )

            if not created:
                cart_item.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
