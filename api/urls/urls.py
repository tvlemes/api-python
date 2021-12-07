from django.contrib import admin
# from core.serializers.tutorial_serializer import TutorialSerializer
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from core.views.user_view import UserViewSet
from core.views.experience_view import ExperienceViewSet
from core.views.favorite_view import FavoriteView
from core.views.course_view import CourseViewSet
from core.views.technology_view import TechnologyViewSet
from core.views.tutorial_view import TutorialViewSet
from api.settings import settings
from django.conf.urls.static import static  

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'experiences', ExperienceViewSet, basename='experiences')
router.register(r'favorites', FavoriteView, basename='favorites')
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'technologias', TechnologyViewSet, basename='technologias')
router.register(r'tutorials', TutorialViewSet, basename='tutorials')

urlpatterns = [
    # Admin URL's
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Others URL's
    path('', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
