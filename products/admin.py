from django.contrib import admin
from .models import Category, Item, Image, Specs, Feedback

admin.site.register(Category)


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


class SpecsInline(admin.TabularInline):
    model = Specs
    extra = 0


class FeedbackInline(admin.TabularInline):
    model = Feedback
    extra = 0


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = (ImageInline, SpecsInline, FeedbackInline)
    ordering = ['category', 'title']