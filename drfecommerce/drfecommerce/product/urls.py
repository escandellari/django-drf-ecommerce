from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from drfecommerce.product import views

router = DefaultRouter()
router.register(r"category", views.CategoryView)
router.register(r"brand", views.BrandView)
router.register(r"product", views.ProductView)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/schema", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/docs", SpectacularSwaggerView.as_view(url_name="schema")),
]
