from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import AmountIngredients, Recipe, Product


def add_product_to_recipe(request,
                          recipe_id,
                          product_id,
                          weight):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    ingredient = get_object_or_404(Product, id=product_id)
    amount, created = AmountIngredients.objects.get_or_create(recipe=recipe,
                                                              product=ingredient,
                                                              )
    amount.weight = weight
    amount.save()
    return HttpResponse('Успешно')


def cook_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    for product in recipe.ingredients.all():
        product.count_of_use = product.count_of_use + 1
        product.save()
    return HttpResponse('Блюдо приготовлено еще раз')


def show_recipes_without_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    recipes_without = Recipe.objects.exclude(ingredients__id=product_id)
    recipes = product.recipe.filter(
        amount_ingredients__weight__lte=10).union(recipes_without)
    return render(
        request,
        'show_recipes_without_product.html',
        {'recipes': recipes})
