from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    pages_count = models.IntegerField(default=0)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    categories = models.ManyToManyField("Category", related_name="books")

    def __str__(self):
        return f"{self.title}"


class Author(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Widget(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True, unique=True)
    metadata_schema = models.JSONField(null=True, blank=True, default=dict)

    def __str__(self):
        return f"{self.name}"


class PageWidget(models.Model):
    page = models.ForeignKey("Page", on_delete=models.CASCADE)
    widget = models.ForeignKey("Widget", on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    metadata = models.JSONField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.page}-{self.widget}"


class Portal(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True, unique=True)

    def __str__(self):
        return f"{self.name}"


class Page(models.Model):
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True)
    slug = models.SlugField(max_length=255, blank=True, null=True, unique=True)
    widgets = models.ManyToManyField(
        "Widget", related_name="pages", through="PageWidget"
    )
    title = models.CharField(max_length=255, blank=True, null=True)
    add_to_menu = models.BooleanField(default=False)
    image = models.CharField(max_length=255, blank=True, null=True)
    portal = models.ForeignKey(
        "Portal", on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self) -> str:
        return f"{self.slug}"
