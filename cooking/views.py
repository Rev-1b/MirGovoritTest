from django.contrib import messages
from django.db.models import F, Q
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, TemplateView

from cooking.models import RecipeModel, ProductModel, RecipeToProductModel


class IndexView(TemplateView):
    template_name = 'cooking/index.html'


class AddProductToRecipeView(View):
    def get(self, request: HttpRequest, *args, **kwargs):

        recipe_obj = get_object_or_404(RecipeModel, id=request.GET.get(key='recipe_id', default=0))
        product_obj = get_object_or_404(ProductModel, id=request.GET.get(key='product_id', default=0))
        weight = request.GET.get(key='weight', default=0)

        recipe_products = RecipeToProductModel.objects.filter(recipe=recipe_obj, product=product_obj)

        if recipe_products.exists():
            recipe_products.update(weight=weight)
            messages.info(request, message=f'Вес продукта "{product_obj}", принадлежащего рецепту "{recipe_obj}" '
                                           f'изменен на {weight} грамм')
        else:
            RecipeToProductModel.objects.create(recipe=recipe_obj, product=product_obj, weight=weight)
            messages.info(request, message=f'Рецепту "{recipe_obj}" добавлено {weight} грамм продукта "{product_obj}"')

        return render(request, 'cooking/index.html')


class CookRecipeView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        recipe_obj = get_object_or_404(RecipeModel, id=request.GET.get(key='recipe_id', default=0))
        recipe_obj.products.update(was_cooked=F('was_cooked') + 1)

        messages.info(request, message=f'Всем продуктам рецепта "{recipe_obj}" в поле "was_cooked" была добавлена 1')

        return render(request, 'cooking/index.html')


class ShowRecipesWithoutProductView(ListView):
    def get_queryset(self):
        product = get_object_or_404(ProductModel, id=self.request.GET.get(key='product_id', default=0))

        query = RecipeModel.objects.filter(
            ~Q(products__in=[product]) |
            (Q(products__in=[product]) &
             Q(products__recipetoproductmodel__weight__lt=10)
             )
        ).distinct().values('id', 'name')

        return query

    template_name = 'cooking/show_recipies.html'
    context_object_name = 'recipes'
