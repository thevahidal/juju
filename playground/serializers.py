from rest_framework import serializers

from playground.models import Book, Page, PageWidget, Widget


class BookListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        # Maps for id->instance and id->data item.
        book_mapping = {book.id: book for book in instance}
        data_mapping = {item["id"]: item for item in validated_data}

        print(book_mapping, data_mapping)

        # Perform creations and updates.
        ret = []
        for book_id, data in data_mapping.items():
            book = book_mapping.get(book_id, None)
            if book is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(book, data))

        # Perform deletions.
        for book_id, book in book_mapping.items():
            if book_id not in data_mapping:
                book.delete()

        return ret


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if not instance:
            raise Exception("WTF?")
        Book.objects.filter(id=instance.id).update(**validated_data)
        instance.refresh_from_db()
        return instance

    class Meta:
        list_serializer_class = BookListSerializer


class PageWidgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageWidget
        fields = ("metadata", "order")


class WidgetSerializer(serializers.ModelSerializer):
    pagewidget_set = PageWidgetSerializer(many=True)

    class Meta:
        model = Widget
        fields = ("slug", "pagewidget_set")


class PagesSerializer(serializers.ModelSerializer):
    widgets = WidgetSerializer(many=True)
    order = serializers.IntegerField(source="widgets_set.order", read_only=True)

    class Meta:
        model = Page
        fields = "__all__"


class MenusSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        children = obj.page_set.filter(add_to_menu=True)
        return MenusSerializer(children, many=True).data

    class Meta:
        model = Page
        fields = ("title", "slug", "children")
