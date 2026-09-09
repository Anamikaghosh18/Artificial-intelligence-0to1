from rest_framework.viewsets import ModelViewSet
from .models import Blog, Comment
from . import serializers
from rest_framework.filters import SearchFilter, OrderingFilter

class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()

    serializer_class = serializers.BlogSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['blog_title', 'blog_body']
    ordering_fields = ['id']


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
