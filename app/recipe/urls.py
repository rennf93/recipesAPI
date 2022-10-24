# pylint: disable=no-member
# pylint: disable=invalid-name
"""
URL mappings for the recipe app.
"""

from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from recipe import views


router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)  # type: ignore

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]
