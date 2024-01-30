from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin

from .models import AmountIngredients, Product, Recipe


class AmountIngredientsInline(admin.TabularInline):
    model = AmountIngredients


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [AmountIngredientsInline, ]


admin.site.register(Product)
