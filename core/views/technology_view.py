from rest_framework import viewsets, status
from rest_framework.response import Response
from core.config_api.technology_crud import TechnologyCrud
from core.serializers.technology_serializer import TechnologySerializer

class TechnologyViewSet(viewsets.ViewSet):
    client = TechnologyCrud('collection_tutorials')

    def list(self, request):
        r = self.client.all()
        serializer = TechnologySerializer(r, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        resumo = self.client.get_by_id(pk)

        if resumo:
            serializer = TechnologySerializer(resumo)
            return Response(serializer.data)

    def create(self, request):
        serializer = TechnologySerializer(data=request.data)
        serializer.is_valid()

        self.client.create(serializer.data)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        serializer = TechnologySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.client.update(pk, serializer.data)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.client.delete_by_id(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
