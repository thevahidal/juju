from django.contrib import admin
from django.db.models import JSONField

from django_json_widget.widgets import JSONEditorWidget

from .models import Book, Author, Category, Page, PageWidget, Portal, Widget


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
    )


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "last_name",
        "first_name",
    )


@admin.register(Portal)
class PortalAdmin(admin.ModelAdmin):
    pass


@admin.register(Widget)
class WidgetAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {"widget": JSONEditorWidget},
    }


@admin.register(PageWidget)
class PageWidgetAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {"widget": JSONEditorWidget},
    }


class PageWidgetInline(admin.TabularInline):
    model = PageWidget
    extra = 0
    formfield_overrides = {
        JSONField: {"widget": JSONEditorWidget},
    }


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    inlines = [PageWidgetInline]
