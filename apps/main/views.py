from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Post
from .serializers import PostSerializer
from django.http import JsonResponse

User = get_user_model()

@api_view(['GET'])
def my_view(request):
    data = {'message': 'Hello, world!'}
    return JsonResponse(data)




