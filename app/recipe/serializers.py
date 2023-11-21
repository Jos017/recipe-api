"""Serializers for recipe APIs."""
from core.models import Recipe, Tag
from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""

    class Meta:
        """Serializer Properties."""

        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail."""

    class Meta(RecipeSerializer.Meta):
        """Serializer Properties."""

        fields = RecipeSerializer.Meta.fields + ['description']


class TagSerializer(serializers.ModelSerializer):
    """Serializer for Tags."""

    class Meta:
        """Tag Serializer Properties."""

        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']
