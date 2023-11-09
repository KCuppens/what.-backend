from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.api.v1.serializers import LoginSerializer


class LoginView(APIView):
    """
    Dummy login API endpoint without validation from the backend
    """

    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"].lower()
            return Response(
                data={"data": {"email": email, "token": "dummy_token"}}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
