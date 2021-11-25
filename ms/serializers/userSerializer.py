from .serializer import Serializer


class UserSerializer(Serializer):
    response = {
        "id": str,
        "phone": str,
        "email": str,
        "name": str,
        "lastname": str,
        "mothername": str
    }
