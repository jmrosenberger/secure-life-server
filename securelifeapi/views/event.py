"""View module for handling requests about events"""
from django.core.exceptions import ValidationError
from rest_framework import status
# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from securelifeapi.models import Event
# from django.contrib.auth import get_user_model


class EventView(ViewSet):
    """SecureLife"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized event instance
        """

        # Uses the token passed in the `Authorization` header
        # image = Image.objects.get(pk=request.data["imageId"])
        # Use the Django ORM to get the record from the database
        # whose `id` is what the client passed as the

        # Try to save the new event to the database, then
        # serialize the event instance as JSON, and send the
        # JSON as a response to the client request
        try:
            # Create a new Python instance of the Event class
            # and set its properties from what was sent in the
            # body of the request from the client.
            event = Event.objects.create(
                title=request.data["title"],
                date=request.data["date"],
                notes=request.data["notes"],
            )
            serializer = EventSerializer(
                event, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # If anything went wrong, catch the exception and
        # send a response with a 400 status code to tell the
        # client that something was wrong with its request data
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        """Handle GET requests for single event

        Returns:
            Response -- JSON serialized event instance
        """
        try:
            # `pk` is a parameter to this function, and
            # Django parses it from the URL route parameter
            #   http://localhost:8000/events/2
            #
            # The `2` at the end of the route becomes `pk`
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(
                event, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """Handle PUT requests for a event

        Returns:
            Response -- Empty body with 204 status code
        """

        # Do mostly the same thing as POST, but instead of
        # creating a new instance of Event, get the Event record
        # from the database whose primary key is `pk`
        event = Event.objects.get(pk=pk)
        event.title = request.data["title"]
        event.date = request.data["date"]
        event.notes = request.data["notes"]
        event.save()

        # 204 status code means everything worked but the
        # server is not sending back any data in the response
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single event

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            event = Event.objects.get(pk=pk)
            event.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Event.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to event resource

        Returns:
            Response -- JSON serialized list of events
        """
        # Get all event records from the database
        # human = Human.objects.get(user=request.auth.user)

        # Support filtering games by type
        #    http://localhost:8000/events?year=1
        #
        # That URL will retrieve all events
        # game_type = self.request.query_params.get('type', None)
        # if game_type is not None:
        #     games = games.filter(game_type__id=game_type)
        event = Event.objects.order_by('date')

        serializer = EventSerializer(
            event, many=True, context={'request': request})
        return Response(serializer.data)


class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for events

    Arguments:
        serializer type
    """

    class Meta:
        model = Event
        fields = ('id', 'title', 'date', 'notes')
        depth = 1
