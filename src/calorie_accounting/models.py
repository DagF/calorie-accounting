#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db.models import Model, CharField, BooleanField, ManyToManyField, ForeignKey, DateTimeField, IntegerField
from django.contrib.auth.models import User


# Create your models here.
class Grocery(Model):
    name = CharField(max_length=256)
    kcal = IntegerField()
    active = BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Ingredient(Model):
    grocery = ForeignKey(Grocery)
    amount_in_grams = IntegerField()

    def __str__(self):
        return self.name


class Meal(Model):
    name = CharField(max_length=256)
    description = CharField(blank=True, max_length=512)
    active = BooleanField(default=True)
    ingredients = ManyToManyField(blank=True, to="Ingredient", related_name="meals")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Consumed(Model):
    created = DateTimeField(auto_now_add=True)
    kcal = IntegerField()
    user = ForeignKey(User)
    meal = ForeignKey(Meal, blank=True, null=True)


class Activity(Model):
    name = CharField(max_length=256)
    created = DateTimeField(auto_now_add=True)
    kcal = IntegerField()
    user = ForeignKey(User)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

