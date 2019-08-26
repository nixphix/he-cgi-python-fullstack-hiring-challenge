from rest_framework import serializers

from games.models import Game


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = (
            'title', 'platform', 'score', 'genre',
            'editors_choice', 'created_at', 'updated_at'
        )
