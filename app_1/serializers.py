from rest_framework.serializers import ModelSerializer
from .models import *

class TodoSerial(ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'sarlavha', 'sana', 'batafsil', 'status']