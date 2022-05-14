from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

from api_app.models import UserModel
from api_app.serializers import UserModelSerializer


class UsersService:
    def create_user(self, data):
        serializer = UserModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data

    def get_users(self, page_number=0, page_size=20):
        users = list(UserModel.objects.all())
        paginator = Paginator(users, page_size)
        return paginator.get_page(page_number)

    def get_user(self, id):
        user = get_object_or_404(UserModel, id=id)
        serializer = UserModelSerializer(user)
        return serializer.data

    def delete_user(self, id):
        user = get_object_or_404(UserModel, id=id)
        user.delete()

    def update_user(self, id, data):
        user = get_object_or_404(UserModel, id=id)
        serializer = UserModelSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return ValidationError("Wrong object")