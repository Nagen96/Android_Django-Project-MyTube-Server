from rest_framework import serializers
from .models import Video, Comment


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['title', 'content', 'video', 'thumbnail', 'videoid']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['commentid', 'token', 'comment', 'videoid']
