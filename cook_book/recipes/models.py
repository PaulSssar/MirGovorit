from django.db import models


class Product(models.Model):
    name = models.CharField(
        'Название продукта',
        max_length=50
    )
    count_of_use = models.IntegerField(
        'Количество раз использовано в рецептах',
        default=0
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Recipe(models.Model):
    name = models.CharField(
        'Название рецепта',
        max_length=50
    )
    ingredients = models.ManyToManyField(
        Product,
        verbose_name='Ингредиент',
        related_name='recipe',
        through='AmountIngredients',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class AmountIngredients(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        verbose_name='Рецепт',
        on_delete=models.CASCADE,
        related_name='amount_ingredients'
    )
    product = models.ForeignKey(
        Product,
        verbose_name='Продукт',
        on_delete=models.CASCADE,
        related_name='amount_ingredients'
    )
    weight = models.IntegerField(
        'Количество',
        null=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('product', 'recipe'),
                name='unique_ingredient_in_recipe'
            )
        ]
