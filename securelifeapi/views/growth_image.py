"""View module for handling requests about pictures"""
import uuid, base64
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.files.base import ContentFile
from securelifeapi.models import GrowthImage, Growth

class GrowthImageView(ViewSet):
    """SecureLife pictures"""

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized image instance
        """

        growth = Growth.objects.get(pk = request.data["growth_id"])
        growth_image = GrowthImage()
        format, imgstr = request.data["action_pic"].split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["growth_id"]}-{uuid.uuid4()}.{ext}')
        growth_image.growth = growth
        growth_image.action_pic = data
        growth_image.save()
        # Try to save the new picture to the database, then
        # serialize the picture instance as JSON, and send the
        # JSON as a response to the client request
        try:
            serializer = GrowthImageSerializer(growth_image, context={'request': request})

            return Response(serializer.data)

        # If anything went wrong, catch the exception and
        # send a response with a 400 status code to tell the
        # client that something was wrong with its request data
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single image
        Returns:
            Response -- JSON serialized image instance
        """
        try:
            image = GrowthImage.objects.get(pk=pk)
            serializer = GrowthImageSerializer(image, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single image
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            image = GrowthImage.objects.get(pk=pk)
            image.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except GrowthImage.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to images resource
        Returns:
            Response -- JSON serialized list of images
        """

        images = GrowthImage.objects.all()
        growth = self.request.query_params.get('growthId', None)
        if growth is not None:
            images = images.filter(growth__id=growth)
        serializer = GrowthImageSerializer(
            images, many=True, context={'request': request})
        return Response(serializer.data)

class GrowthImageSerializer(serializers.ModelSerializer):
    """JSON serializer for images
    Arguments:
        serializer type
    """

    class Meta:
        model = GrowthImage
        fields = ('id', 'growth', 'action_pic')
        depth = 1
        