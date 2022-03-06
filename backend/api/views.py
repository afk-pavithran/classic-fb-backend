from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework import status

# Create your views here.
class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status= status.HTTP_201_CREATED)
        return Response({'status': 'failed', 'error': serializer.errors}, status= status.HTTP_400_BAD_REQUEST)

    def get(self, request, user=None):
        if user:
            item = User.objects.get(user_name=user)
            serializer = UserSerializer(item)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        items = User.objects.all()
        serializer = UserSerializer(items, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
