from django.contrib import admin
from .models import Grocery, Ingredient, Meal, Consumed, Activity

# Register your models here.



admin.site.register(Grocery)
admin.site.register(Ingredient)
admin.site.register(Meal)
admin.site.register(Consumed)
admin.site.register(Activity)