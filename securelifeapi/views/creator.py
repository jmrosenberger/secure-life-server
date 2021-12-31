"""View module for handling requests about creators"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from securelifeapi.models import Creator
from rest_framework import status
from securelifeapi.serializers import CreatorSerializer
# from django.contrib.auth.models import User


class CreatorView(ViewSet):
    """SecureLife Creator profile"""

    def list(self, request):
        """Handle GET requests for single creator
        Returns:
        Response -- JSON serialized event
        """
        try:
            creator = Creator.objects.get(user=request.auth.user)
            serializer = CreatorSerializer(
                creator, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)
