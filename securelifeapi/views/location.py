"""View module for handling requests about games"""
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from securelifeapi.models import Adventure, Human, Image, PlacesVisited, Location, Park, City, State, Country, Tag

class LocationView(ViewSet):
    """SecureLife"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized location instance
        """

        # Uses the token passed in the `Authorization` header
        human = Human.objects.get(user=request.auth.user)
        
        # image = Image.objects.get(pk=request.data["imageId"])

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
            location = Location.objects.create(
                city=request.data["city"],
                park=request.data["park"]
            )
            serializer = LocationSerializer(location, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # If anything went wrong, catch the exception and
        # send a response with a 400 status code to tell the
        # client that something was wrong with its request data
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)



    def retrieve(self, request, pk):
        """Handle GET requests for single location

        Returns:
            Response -- JSON serialized location instance
        """
        try:
            # `pk` is a parameter to this function, and
            # Django parses it from the URL route parameter
            #   http://localhost:8000/games/2
            #
            # The `2` at the end of the route becomes `pk`
            location = Location.objects.get(pk=pk)
            serializer = LocationSerializer(location, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """Handle PUT requests for a location

        Returns:
            Response -- Empty body with 204 status code
        """
        human = Human.objects.get(user=request.auth.user)
        
        # image = Image.objects.get(pk=request.data["imageId"])

        # Do mostly the same thing as POST, but instead of
        # creating a new instance of location, get the location record
        # from the database whose primary key is `pk`
        location = Location.objects.get(pk=pk)
        location.city = request.data["city"]
        location.park = request.data["park"]
        location.save()

        # 204 status code means everything worked but the
        # server is not sending back any data in the response
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single location

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            location = Location.objects.get(pk=pk)
            location.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Location.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to location resource

        Returns:
            Response -- JSON serialized list of locations
        """
        # Get all location records from the database
        human = Human.objects.get(user=request.auth.user)


        # Support filtering locations by type
        #    http://localhost:8000/games?type=1
        #
        # That URL will retrieve all tabletop games
        # game_type = self.request.query_params.get('type', None)
        # if game_type is not None:
        #     games = games.filter(game_type__id=game_type)
        location = Location.objects.all()

        serializer = LocationSerializer(
            location, many=True, context={'request': request})
        return Response(serializer.data)


class LocationSerializer(serializers.ModelSerializer):
    """JSON serializer for locations

    Arguments:
        serializer type
    """
    class Meta:
        model = Location
        fields = ('id', 'city', 'park')
        depth = 1
