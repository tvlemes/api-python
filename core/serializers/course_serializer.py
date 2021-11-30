from rest_framework import serializers

class CourseSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100, read_only=True)
    name = serializers.CharField()
    institution = serializers.CharField()
    workload = serializers.CharField()
    briefsummary = serializers.CharField()
    content = serializers.CharField()
    start_date = serializers.DateTimeField()
    departure_date = serializers.DateTimeField()
    url_image = serializers.CharField()
    tags = serializers.CharField()