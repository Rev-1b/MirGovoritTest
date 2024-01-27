from django.db import models


class ProductModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название продукта')
    was_cooked = models.IntegerField(default=0, verbose_name='Количество использований продукта в рецептах')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class RecipeModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название рецепта')
    products = models.ManyToManyField(to='ProductModel', through='RecipeToProductModel')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class RecipeToProductModel(models.Model):
    recipe = models.ForeignKey(to=RecipeModel, on_delete=models.CASCADE, verbose_name='Объект рецепта')
    product = models.ForeignKey(to=ProductModel, on_delete=models.CASCADE, verbose_name='Объект продукта')
    weight = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Cвязь рецепт-продукт'
        verbose_name_plural = 'Cвязи рецепт-продукт'

    def __str__(self):
        return f'{self.product.name} В {self.recipe.name}'


