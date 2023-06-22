from .models import User
from .serializers import UserSerializer
from  rest_framework import generics
# Create your views here.

class CreateListUserView(generics.CreateAPIView):
        serializer_class= UserSerializer
        queryset = User.objects.all()

        def perform_create(self, serializer):
                instance = serializer.save()
                instance.set_password(instance.password)
                instance.save()

        
