from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = [
            'id',
            'post',
            'author',
            'author_username',
            'text',
            'created_at',
        ]
        read_only_fields = ['author', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'owner',
            'owner_username',
            'image',
            'caption',
            'created_at',
            'comments',
        ]
        read_only_fields = ['owner', 'created_at']

