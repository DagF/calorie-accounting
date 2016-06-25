from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import GrocerySerializer, IngredientSerializer, MealSerializer, ConsumedSerializer, ActivitySerializer
from ..models import Grocery, Ingredient, Meal, Consumed, Activity


class GroceryViewSet(GenericViewSet, CreateModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin):
    serializer_class = GrocerySerializer
    queryset = Grocery.objects.all()
    authentication_classes = (BasicAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)


class IngredientViewSet(GenericViewSet, CreateModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    permission_classes = (IsAuthenticated,)
    filter_fields = ('active',)


class MealViewSet(GenericViewSet, CreateModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()
    permission_classes = (IsAuthenticated,)
    filter_fields = ('active',)


class ConsumedViewSet(GenericViewSet, CreateModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin):
    serializer_class = ConsumedSerializer
    queryset = Consumed.objects.all()
    permission_classes = (IsAuthenticated,)
    filter_fields = ('active',)


class ActivityViewSet(GenericViewSet, CreateModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    permission_classes = (IsAuthenticated,)
    filter_fields = ('active',)
