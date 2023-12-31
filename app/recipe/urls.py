"""URL mappings for the recipe app."""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()
router.register('ingredients', views.IngredientViewSet)
router.register('tags', views.TagViewSet)
router.register('', views.RecipeViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]
