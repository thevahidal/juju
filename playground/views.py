from rest_framework import generics, mixins, views, viewsets
from rest_framework.response import Response

from juju.views import CRUDView

from playground.models import Book, Page
from playground.serializers import BookSerializer, MenusSerializer, PagesSerializer


class BooksView(CRUDView):
    model = Book


class BulkBooksView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset, data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class PagesView(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PagesSerializer
    lookup_field = "slug"


class MenusView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Page.objects.filter(add_to_menu=True, parent=None)
    print(queryset)
    serializer_class = MenusSerializer

    def get_queryset(self):
        portal = self.request.query_params.get("portal", None)

        if portal:
            return self.queryset.filter(portal__slug=portal)

        return self.queryset
