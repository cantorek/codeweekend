from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Idea, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username')

class IdeaSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Idea
        fields = ('url', 'author', 'title', 'description', 'difficulty', 'date_added')
