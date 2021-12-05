from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from core.views.user_view import UserViewSet
from core.views.experience_view import ExperienceViewSet
from core.views.favorite_view import FavoriteView
from core.views.course_view import CourseViewSet
from core.views.technology_view import TechnologyViewSet
from api.settings import settings
from django.conf.urls.static import static  

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'experiences', ExperienceViewSet, basename='experiences')
router.register(r'favorites', FavoriteView, basename='favorites')
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'technologias', TechnologyViewSet, basename='technologias')

urlpatterns = [
    # Admin URL's
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Others URL's
    path('', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
