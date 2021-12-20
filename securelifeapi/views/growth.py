"""View module for handling requests about growth"""
from django.core.exceptions import ValidationError
from rest_framework import status
# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from securelifeapi.models import Growth, Human
# from django.contrib.auth import get_user_model


class GrowthView(ViewSet):
    """SecureLife"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized growth instance
        """

        # Uses the token passed in the `Authorization` header
        human = Human.objects.get(pk=request.data['human'])
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
            growth = Growth.objects.create(
                human=human,
                age=request.data["age"],
                height=request.data["height"],
                weight=request.data["weight"],
                length=request.data["length"],
                date=request.data["date"],
                notes=request.data["notes"]
            )
            # adventure.participants.set(human)
            serializer = GrowthSerializer(
                growth, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # If anything went wrong, catch the exception and
        # send a response with a 400 status code to tell the
        # client that something was wrong with its request data
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        """Handle GET requests for single growth entry

        Returns:
            Response -- JSON serialized growth instance
        """
        try:
            # `pk` is a parameter to this function, and
            # Django parses it from the URL route parameter
            #   http://localhost:8000/games/2
            #
            # The `2` at the end of the route becomes `pk`
            growth = Growth.objects.get(pk=pk)
            serializer = GrowthSerializer(
                growth, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """Handle PUT requests for a growth entry

        Returns:
            Response -- Empty body with 204 status code
        """
        # human = Human.objects.get(user=request.auth.user)
        # image = Image.objects.get(pk=request.data["imageId"])
        human = Human.objects.get(pk=request.data['human']['id'])

        # Do mostly the same thing as POST, but instead of
        # creating a new instance of Game, get the game record
        # from the database whose primary key is `pk`
        growth = Growth.objects.get(pk=pk)
        growth.human = human
        growth.age=request.data["age"]
        growth.height=request.data["height"]
        growth.weight=request.data["weight"]
        growth.length=request.data["length"]
        growth.date=request.data["date"]
        growth.notes=request.data["notes"]
        growth.save()

        # 204 status code means everything worked but the
        # server is not sending back any data in the response
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single growth

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            growth = Growth.objects.get(pk=pk)
            growth.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Growth.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to growth resource

        Returns:
            Response -- JSON serialized list of growths
        """
        # Get all growth records from the database
        # human = Human.objects.get(user=request.auth.user)
        # growth = growth.objects.annotate(event_count=Count('events'))

        # Support filtering games by type
        #    http://localhost:8000/games?type=1
        #
        # That URL will retrieve all tabletop games
        # game_type = self.request.query_params.get('type', None)
        # if game_type is not None:
        #     games = games.filter(game_type__id=game_type)
        growth = Growth.objects.all()

        serializer = GrowthSerializer(
            growth, many=True, context={'request': request})
        return Response(serializer.data)

class HumanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Human
        fields = ['name']


class GrowthSerializer(serializers.ModelSerializer):
    """JSON serializer for growth entries

    Arguments:
        serializer type
    """

    class Meta:
        model = Growth
        fields = ('id', 'human', 'age', 'height', 'weight', 'length', 'date', 'notes')
        depth = 1
