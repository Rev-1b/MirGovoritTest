from django.contrib import admin
from cooking.models import *


class Relation(admin.TabularInline):
    model = RecipeModel.products.through


@admin.register(RecipeModel)
class RecipeModelAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    inlines = [
        Relation
    ]


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    readonly_fields = ['id']

admin.site.register(RecipeToProductModel)
