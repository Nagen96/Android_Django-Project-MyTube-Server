from rest_framework import serializers
from .models import Video, Comment


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['title', 'content', 'video', 'thumbnail']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['token', 'comment', 'url']
