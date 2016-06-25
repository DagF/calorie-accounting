from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer
from ..models import Grocery, Ingredient, Meal, Consumed, Activity
from django.contrib.auth.models import User


class GrocerySerializer(ModelSerializer):

    class Meta(object):
        model = Grocery
        fields = ('id', 'name', 'kcal', 'active')


class IngredientSerializer(ModelSerializer):

    class Meta(object):
        model = Ingredient
        fields = ('id', 'grocery', 'amount_in_grams')


class MealSerializer(ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    def create(self, validated_data):
        ingredients = validated_data.pop('ingredients')
        meal = Meal.objects.create(**validated_data)
        for ingredient in ingredients:
            ingr = Ingredient.objects.create(**ingredient)
            meal.ingredients.add(ingr)
        meal.save()
        return meal

    class Meta(object):
        model = Meal
        fields = ('id', 'name', 'description', 'active', 'ingredients')


class ActivitySerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta(object):
        model = Activity
        fields = ('id', 'name', 'created', 'kcal', 'user')


class ConsumedSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(queryset=User.objects.all())
    meal = PrimaryKeyRelatedField(queryset=Meal.objects.all())

    class Meta(object):
        model = Consumed
        fields = ('id', 'created', 'kcal', 'user', 'meal')


