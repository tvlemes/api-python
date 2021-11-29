from rest_framework import viewsets, status
from rest_framework.response import Response
from core.config_api.experience_crud import ExperienceCrud
from core.serializers.experience_serializer import ExperienceSerializer

class ExperienceViewSet(viewsets.ViewSet):
    client = ExperienceCrud('collection_professional_experience')

    def list(self, request):
        r = self.client.all()
        serializer = ExperienceSerializer(r, many=True)
        return Response(serializer.data)
    
    # @login_required(login_url='/login/')
    def retrieve(self, request, pk=None):
        resumo = self.client.get_by_id(pk)

        if resumo:
            serializer = ExperienceSerializer(resumo)
            return Response(serializer.data)

    # @login_required(login_url='/login/')
    def create(self, request):
        serializer = ExperienceSerializer(data=request.data)
        serializer.is_valid()

        self.client.create(serializer.data)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    # @login_required(login_url='/login/')
    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        serializer = ExperienceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.client.update(pk, serializer.data)

        return Response(serializer.data)

    # @login_required(login_url='/login/')
    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.client.delete_by_id(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
