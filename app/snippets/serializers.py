from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['id', 'owner', 'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
