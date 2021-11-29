from rest_framework import serializers

class FavoritesSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100, read_only=True)
    name = serializers.CharField()
    url_name = serializers.CharField()
    url_image = serializers.CharField()
    briefsummary = serializers.CharField()
    tags = serializers.CharField()
    favorites = serializers.BooleanField() 