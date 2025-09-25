from django.contrib import admin
from .models import Category, ImagePrompt   # ⚡ Note: class name must match your models.py

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at", "updated_at")   # columns in admin list
    search_fields = ("name", "slug")                             # search bar
    prepopulated_fields = {"slug": ("name",)}                     # auto-fill slug from name
    ordering = ("name",)                                          # order categories


@admin.register(ImagePrompt)   # ⚡ Make sure it matches exactly (Imageprompt not ImagePrompt)
class ImagePromptAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_trending", "created_at")  # ❌ removed "like"
    list_filter = ("category", "is_trending")                          # sidebar filter
    search_fields = ("title", "prompt")                                # search bar
    ordering = ("-created_at",)                                        # ✅ must be a tuple
                                       

