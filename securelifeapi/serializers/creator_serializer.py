from rest_framework import serializers
from django.contrib.auth import get_user_model
from securelifeapi.models import Creator


class UserSerializer (serializers.ModelSerializer):
    """JSON serializer for locations

    Arguments:
        serializer type
    """
    class Meta:
        model = get_user_model()
        fields = ('username',)


class CreatorSerializer (serializers.ModelSerializer):
    """JSON serializer for locations

    Arguments:
        serializer type
    """
    user = UserSerializer()

    class Meta:
        model = Creator
        fields = ('user')
        depth = 1
        