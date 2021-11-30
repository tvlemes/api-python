from rest_framework import viewsets, status
from rest_framework.response import Response
from core.config_api.favorite_crud import FavoriteCrud
from core.serializers.favorite_serializer import FavoriteSerializer
from rest_framework.exceptions import NotFound

class FavoriteView(viewsets.ViewSet):
    
    client = FavoriteCrud('collection_favorites')

    def list(self, request):
        r = self.client.all()
        serializer = FavoriteSerializer(r, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        favorites = self.client.get_by_id(pk)

        if favorites:
            serializer = FavoriteSerializer(favorites)
            return Response(serializer.data)

    def create(self, request):
        if request.method == 'POST':
            serializer = FavoriteSerializer(data=request.data)
            serializer.is_valid()

            self.client.create(serializer.data)

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        serializer = FavoriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.client.update(pk, serializer.data)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.client.delete_by_id(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
