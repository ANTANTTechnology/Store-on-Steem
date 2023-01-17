from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class LevelofDifficultyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id','title','price','is_published',)
    list_display_links = ('title',)
    search_fields = ('title','product_id')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(LevelofDifficulty, LevelofDifficultyAdmin)
admin.site.register(Product, ProductAdmin)