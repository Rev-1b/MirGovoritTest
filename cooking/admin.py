from django.contrib import admin
from cooking.models import *


class Relation(admin.TabularInline):
    model = RecipeModel.products.through


@admin.register(RecipeModel)
class RecipeModelAdmin(admin.ModelAdmin):
    inlines = [
        Relation
    ]


admin.site.register(ProductModel)
admin.site.register(RecipeToProductModel)
