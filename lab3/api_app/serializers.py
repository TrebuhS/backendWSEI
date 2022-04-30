from rest_framework import serializers
from .models import UserModel

class UserModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
        model = UserModel
        fields = ('__all__')