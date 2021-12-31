"""View module for handling requests about games"""
from django.core.exceptions import ValidationError
from rest_framework import status
# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from securelifeapi.models import Human, Creator
# from django.contrib.auth import get_user_model

class HumanView(ViewSet):
    """SecureLife"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """

        # Uses the token passed in the `Authorization` header
        creator = Creator.objects.get(user=request.auth.user)
        # # image = Image.objects.get(pk=request.data["imageId"])

        # Use the Django ORM to get the record from the database
        # whose `id` is what the client passed as the
        # `gameTypeId` in the body of the request.
        # game_type = GameType.objects.get(pk=request.data["gameTypeId"])

        # Try to save the new game to the database, then
        # serialize the game instance as JSON, and send the
        # JSON as a response to the client request
        try:
            # Create a new Python instance of the Adventure class
            # and set its properties from what was sent in the
            # body of the request from the client.
            human = Human.objects.create(
                creator=creator,
                name=request.data["name"]
            )
            serializer = HumanSerializer(human, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # If anything went wrong, catch the exception and
        # send a response with a 400 status code to tell the
        # client that something was wrong with its request data
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)



    def retrieve(self, request, pk):
        """Handle GET requests for single human

        Returns:
            Response -- JSON serialized human instance
        """
        try:
            # `pk` is a parameter to this function, and
            # Django parses it from the URL route parameter
            #   http://localhost:8000/games/2
            #
            # The `2` at the end of the route becomes `pk`
            human = Human.objects.get(pk=pk)
            serializer = HumanSerializer(human, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """Handle PUT requests for a human

        Returns:
            Response -- Empty body with 204 status code
        """
        creator = Creator.objects.get(user=request.auth.user)
        # image = Image.objects.get(pk=request.data["imageId"])
        # Do mostly the same thing as POST, but instead of
        # creating a new instance of Game, get the game record
        # from the database whose primary key is `pk`
        human = Human.objects.get(pk=pk)
        human.creator = creator
        human.name = request.data["name"]
        human.save()

        # 204 status code means everything worked but the
        # server is not sending back any data in the response
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single human

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            human = Human.objects.get(pk=pk)
            human.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Human.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to human resource

        Returns:
            Response -- JSON serialized list of humans
        """
        # Get all adventure records from the database
        creator = Creator.objects.get(user=request.auth.user)
        # adventure = Adventure.objects.annotate(event_count=Count('events'))


        # Support filtering games by type
        #    http://localhost:8000/games?type=1
        #
        # That URL will retrieve all tabletop games
        # game_type = self.request.query_params.get('type', None)
        # if game_type is not None:
        #     games = games.filter(game_type__id=game_type)
        human = Human.objects.filter(creator=creator)

        serializer = HumanSerializer(
            human, many=True, context={'request': request})
        return Response(serializer.data)
class CreatorSerializer(serializers.ModelSerializer):
    """JSON serializer for creator

    Arguments:
        serializer type
    """

    class Meta:
        model = Creator
        fields = ['id']

class HumanSerializer(serializers.ModelSerializer):
    """JSON serializer for humans

    Arguments:
        serializer type
    """
    creator = CreatorSerializer(many=False)

    class Meta:
        model = Human
        fields = ('id', 'creator', 'name')
        depth = 1
