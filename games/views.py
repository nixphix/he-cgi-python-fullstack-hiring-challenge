from rest_framework import filters
from rest_framework import viewsets
from rest_framework import views

from games.models import Game
from games.serializers import GameSerializer


class GameModelViewSet(viewsets.ModelViewSet):
    search_fields = ["title"]
    filter_backends = (filters.SearchFilter,)
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    # permission_classes = [IsAccountAdminOrReadOnly]


class GameModelCSVUploadView(views.APIView):

    def post(self, request):
        file = request.FILES

