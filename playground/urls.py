from rest_framework.routers import DefaultRouter

from .views import MenusView, PagesView

router = DefaultRouter()

router.register("pages", PagesView, basename="pages")
router.register("menus", MenusView, basename="menus")


urlpatterns = [] + router.urls
