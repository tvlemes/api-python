from rest_framework import serializers

class ExperienceSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100, read_only=True)
    company = serializers.CharField()
    occupation = serializers.CharField()
    briefsummary = serializers.CharField()
    activities = serializers.CharField()
    tags = serializers.CharField()
    start_date = serializers.DateTimeField()
    departure_date = serializers.DateTimeField()