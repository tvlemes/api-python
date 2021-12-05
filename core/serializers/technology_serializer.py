from rest_framework import serializers

class TechnologySerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100, read_only=True)
    name = serializers.CharField()
    subtype = serializers.CharField()
    description = serializers.CharField()
    