from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from core.views.user_view import UserViewSet
from core.views.experience_view import ExperienceViewSet
from core.views.favorites_view import FavoritesView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'experiences', ExperienceViewSet, basename='experiences')
router.register(r'favorites', FavoritesView, basename='favorites')

urlpatterns = [
    # Admin URL's
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # path('experiences/', ExperienceViewSet.list),
    # path('experiences/<pk>/', ExperienceViewSet.retrieve),

    # Others URL's
    path('', include(router.urls)),
]
