from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from .models import UserModel
from .serializers import UserModelSerializer
from .service import UsersService


class UserViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    service = UsersService()

    @action(methods=['post'], detail=False, url_path='create')
    def create_user(self, request):
        user = self.service.create_user(request.data)
        return Response(user, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def get_user(self, request, page_number=None, page_size=None):
        page_number = request.Get.get('page_number')
        page_size = request.Get.get('page_size')
        users = self.service.get_users(page_number, page_size)
        return Response(users, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path=r'(?P<id>\w+)')
    def get_user(self, request, id):
        user = self.service.get_user(id)
        return Response(user, status=status.HTTP_200_OK)

    @action(methods=['delete'], detail=False, url_path=r'(?P<id>\w+)/remove')
    def delete_user(self, request, id):
        self.service.delete_user(id)
        return Response({"result": True})

    @action(methods=['patch'], detail=False, url_path=r'(?P<id>\w+)/update')
    def delete_user(self, request, id):
        try:
            user = self.service.update_user(id, request.data)
            return Response(user, status=status.HTTP_200_OK)
        except ValidationError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return