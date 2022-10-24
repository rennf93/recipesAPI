# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=no-member
# pylint: disable=undefined-variable
"""
Serializers for recipe APIs
"""

from decimal import Decimal
from rest_framework import serializers

from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail view."""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']

    def test_create_recipe(self):
        """Test creating a recipe."""

        payload = {
            'title': 'Sample recipe',
            'time_minutes': 30,
            'price': Decimal('5.99'),
        }
        res = self.client.post(RECIPES_URL, payload)  # type: ignore

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)  # type: ignore
        recipe = Recipe.objects.get(id=res.data['id'])
        for k, v in payload.items():
            self.assertEqual(getattr(recipe, k), v)  # type: ignore
        self.assertEqual(recipe.user, self.user)  # type: ignore
