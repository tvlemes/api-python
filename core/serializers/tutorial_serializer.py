from rest_framework import serializers

class TutorialSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100, read_only=True)
    name = serializers.CharField()
    technology = serializers.CharField()
    description = serializers.CharField()
    markdown = serializers.CharField()
    tags = serializers.CharField()
    