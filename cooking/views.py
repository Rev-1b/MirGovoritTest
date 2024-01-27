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

        recipe_product = RecipeToProductModel.objects.filter(recipe=recipe_obj, product=product_obj).first()

        if recipe_product is None:
            RecipeToProductModel.objects.create(recipe=recipe_obj, product=product_obj,
                                                weight=request.GET.get(key='weight', default=0))
        else:
            recipe_product.weight = request.GET.get(key='weight', default=0)
            recipe_product.save()

        return render(request, 'cooking/index.html')


class CookRecipeView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        recipe_obj = get_object_or_404(RecipeModel, id=request.GET.get(key='recipe_id', default=0))
        recipe_obj.products.update(was_cooked=F('was_cooked') + 1)

        return render(request, 'cooking/index.html')


class ShowRecipesWithoutProductView(ListView):
    def get_queryset(self):
        product_id = self.request.GET.get(key='product_id', default=0)

        return RecipeToProductModel.objects.filter(
            ~Q(product_id=product_id) | (Q(product_id=product_id) &
                                         Q(weight__lt=10))).values('recipe_id', 'recipe__name').distinct()

    template_name = 'cooking/show_recipies.html'
    context_object_name = 'recipes'
