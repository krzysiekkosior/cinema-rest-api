from rest_framework import serializers

from showtimes.models import Cinema


class CinemaSerializer(serializers.ModelSerializer):
    movies = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='cinema-detail'
    )

    class Meta:
        model = Cinema
        fields = '__all__'
