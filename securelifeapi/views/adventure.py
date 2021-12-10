"""View module for handling requests about games"""
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from securelifeapi.models import Adventure, Human, Image, PlacesVisited, Location, Park, City, State, Country, Tag
from django.db.models import Count
from django.contrib.auth.models import User


class AdventureView(ViewSet):
    """SecureLife"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """

        # Uses the token passed in the `Authorization` header
        human = Human.objects.get(user=request.auth.user)
        
        image = Image.objects.get(pk=request.data["imageId"])

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
            adventure = Adventure.objects.create(
                title=request.data["title"],
                human=human,
                date=request.data["date"],
                description=request.data["description"],
                image=image
            )
            serializer = AdventureSerializer(adventure, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # If anything went wrong, catch the exception and
        # send a response with a 400 status code to tell the
        # client that something was wrong with its request data
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)



    def retrieve(self, request, pk):
        """Handle GET requests for single adventure

        Returns:
            Response -- JSON serialized game instance
        """
        try:
            # `pk` is a parameter to this function, and
            # Django parses it from the URL route parameter
            #   http://localhost:8000/games/2
            #
            # The `2` at the end of the route becomes `pk`
            adventure = Adventure.objects.get(pk=pk)
            serializer = AdventureSerializer(adventure, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """Handle PUT requests for a adventure

        Returns:
            Response -- Empty body with 204 status code
        """
        human = Human.objects.get(user=request.auth.user)
        
        image = Image.objects.get(pk=request.data["imageId"])

        # Do mostly the same thing as POST, but instead of
        # creating a new instance of Game, get the game record
        # from the database whose primary key is `pk`
        adventure = Adventure.objects.get(pk=pk)
        adventure.title = request.data["title"]
        adventure.human = human
        adventure.date = request.data["date"]
        adventure.description = request.data["description"]
        adventure.image = image
        adventure.save()

        # 204 status code means everything worked but the
        # server is not sending back any data in the response
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single adventure

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            adventure = Adventure.objects.get(pk=pk)
            adventure.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Adventure.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to adventure resource

        Returns:
            Response -- JSON serialized list of adventures
        """
        # Get all adventure records from the database
        human = Human.objects.get(user=request.auth.user)
        # adventure = Adventure.objects.annotate(event_count=Count('events'))


        # Support filtering games by type
        #    http://localhost:8000/games?type=1
        #
        # That URL will retrieve all tabletop games
        # game_type = self.request.query_params.get('type', None)
        # if game_type is not None:
        #     games = games.filter(game_type__id=game_type)
        adventure = Adventure.objects.all()

        serializer = AdventureSerializer(
            adventure, many=True, context={'request': request})
        return Response(serializer.data)


class AdventureSerializer(serializers.ModelSerializer):
    """JSON serializer for games

    Arguments:
        serializer type
    """
    class Meta:
        model = Adventure
        fields = ('id', 'title', 'human_id', 'date', 'description', 'image_id')
        depth = 1