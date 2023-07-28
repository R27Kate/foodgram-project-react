from rest_framework.routers import DefaultRouter

from recipes.views import TagViewSet, IngredientViewSet, RecipeViewSet

tags_router = DefaultRouter()
tags_router.register('tags', TagViewSet)

ingredients_router = DefaultRouter()
ingredients_router.register('ingredients', IngredientViewSet)

recipes_router = DefaultRouter()
recipes_router.register('recipes', RecipeViewSet)

urlpatterns = [
    *tags_router.urls,
    *ingredients_router.urls,
    *recipes_router.urls
]
