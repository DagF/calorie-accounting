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
        extra_kwargs = {'id': {'read_only': False}}

    def update(self, instance, validated_data):
        print(instance)


class MealSerializer(ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    def create(self, validated_data):
        ingredients = validated_data.pop('ingredients')
        meal = Meal.objects.create(**validated_data)
        for ingredient in ingredients:
            ingr = Ingredient.objects.create(**ingredient)
            meal.ingredients.add(ingr)
        #meal.save()
        return meal

    def update(self,instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)

        ingredients = validated_data.pop('ingredients')
        for ingredient in ingredients:
            ingr = Ingredient.objects.get(id=ingredient.get('id'))
            ingr.amount_in_grams = ingredient.get('amount_in_grams', ingr.amount_in_grams)
            ingr.save()

        instance.save() 
        return instance

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


