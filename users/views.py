from .models import User

from rest_framework import generics, permissions
from serializers import CreateUserSerializer

# Create your views here.


class UserView(generics.ListCreateAPIView):
    """
        Service for user list and creation
        :allowed methods
            GET
            POST
    """
    serializer_class = CreateUserSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
