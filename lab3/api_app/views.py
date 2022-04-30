from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from .models import UserModel
from .serializers import UserModelSerializer
from rest_framework.decorators import action


class UserViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    def get_queryset(self):
        return
    @action(methods=['post'], detail=False, url_path='create')
    def create_user(self, request):
        serializer = UserModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def get_user(self, request, page_number=0, page_size=20):
        page_number = request.Get.get('page_number')
        page_size = request.Get.get('page_size')
        queryset = UserModel.objects.all()
        paginator = Paginator(queryset, page_size)
        return Response({"status": "success", "data": paginator.page(page_number)}, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path=r'(?P<id>\w+)')
    def get_user(self, request, id):
        user = get_object_or_404(UserModel, id=id)
        serializer = UserModelSerializer(user)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    @action(methods=['delete'], detail=False, url_path=r'(?P<id>\w+)/remove')
    def delete_user(self, request, id):
        user = get_object_or_404(UserModel, id=id)
        user.delete()
        return Response({"result": True})

    @action(methods=['patch'], detail=False, url_path=r'(?P<id>\w+)/update')
    def delete_user(self, request, id):
        user = get_object_or_404(UserModel, id=id)
        serializer = UserModelSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)