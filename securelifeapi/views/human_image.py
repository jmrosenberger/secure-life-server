"""View module for handling requests about pictures"""
import uuid, base64
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.files.base import ContentFile
from securelifeapi.models import Human, HumanImage

class HumanImageView(ViewSet):
    """SecureLife pictures"""

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized image instance
        """

        human = Human.objects.get(pk = request.data["human_id"])
        human_image = HumanImage()
        format, imgstr = request.data["action_pic"].split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["human_id"]}-{uuid.uuid4()}.{ext}')
        human_image.human = human
        human_image.action_pic = data
        human_image.save()
        # Try to save the new picture to the database, then
        # serialize the picture instance as JSON, and send the
        # JSON as a response to the client request
        try:
            serializer = HumanImageSerializer(human_image, context={'request': request})

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
            image = HumanImage.objects.get(pk=pk)
            serializer = HumanImageSerializer(image, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single image
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            image = HumanImage.objects.get(pk=pk)
            image.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except HumanImage.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to images resource
        Returns:
            Response -- JSON serialized list of images
        """

        images = HumanImage.objects.all()
        human = self.request.query_params.get('humanId', None)
        if human is not None:
            images = images.filter(human__id=human)
        serializer = HumanImageSerializer(
            images, many=True, context={'request': request})
        return Response(serializer.data)

class HumanImageSerializer(serializers.ModelSerializer):
    """JSON serializer for images
    Arguments:
        serializer type
    """

    class Meta:
        model = HumanImage
        fields = ('id', 'human', 'action_pic')
        depth = 1
        