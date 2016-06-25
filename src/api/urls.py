from rest_framework.routers import DefaultRouter

#

from calorie_accounting.api import views as calorie_accounting_views

router = DefaultRouter()

router.register('groceries', calorie_accounting_views.GroceryViewSet)
router.register('ingredients', calorie_accounting_views.IngredientViewSet)
router.register('meals', calorie_accounting_views.MealViewSet)
router.register('consumed', calorie_accounting_views.ConsumedViewSet)
router.register('activities', calorie_accounting_views.ActivityViewSet)


urlpatterns = router.urls