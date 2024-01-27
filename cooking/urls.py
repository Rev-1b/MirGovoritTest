from django.urls import path
from cooking.views import IndexView, AddProductToRecipeView, CookRecipeView, ShowRecipesWithoutProductView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add_product_to_recipe/', AddProductToRecipeView.as_view(), name='add_product'),
    path('cook_recipe/', CookRecipeView.as_view(), name='cook'),
    path('show_recipes_without_product/', ShowRecipesWithoutProductView.as_view(), name='show_recipes')
]
