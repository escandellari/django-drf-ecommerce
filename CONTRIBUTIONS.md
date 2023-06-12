# What is OpenAPI

The OpenAPI Specification (OAS) provides a consistent means to carry information through each stage of the API lifecycle. It is a specification language for HTTP APIs that defines structure and syntax in a way that is not wedded to the programming language the API is created in. API specifications are typically written in YAML or JSON, allowing for easy sharing and consumption of the specification.

API specification languages provide a standardized means to do this. Your APIs can be described in agnostic terms, decoupling them from any specific programming language. Consumers of your API specification do not need to understand the guts of your application or try to learn Lisp or Haskell if that’s what you chose to write it in. They can understand exactly what they need from your API specification, written in a simple and expressive language.

# Django Rest Framework (DRF)

The Django Rest Framework is a third-party package that empowers a Django app with REST API capabilities.

To install the package, run the command:

```bash
pip install django-rest-framework
```

Add 'rest_framework' to your INSTALLED_APPS setting.

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

## DRF Serializers

DRF serializers convert Django data types, such as querysets, into a format that can be rendered into JSON or XML. In your app folder, create a file named serializers.py and add the code block below.

As an example, `Product` is the name of the model

```python
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        # this is the model that is being serialized
        model = Product
        # if you need all the data from the model, if not create a list
        fields = "__all__"
```

## API Requests

To service a GET or POST request, you need a view that will return all the data in a serialized fashion. To achieve this, create a view within the views.py file and add the view that will return the data, serialized.

```python
class ProductViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing product data
    """

    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
```

## URL Configuration

To configure the URL, configure the main project's urls.py file to direct any traffic to the app using the path function, as in the codeblock below.

```python
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
]
```

In the urls.py file specific for the app, using the path, direct the traffic to your view function.

```python
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"product", views.ProductView)

urlpatterns = [
    path("product/", product, name="product"),
    path("api/", include(router.urls)),
]
```

# DRF Spectacular (DRF)

Sane and flexible OpenAPI 3.0 schema generation for Django REST framework.

To install the package, run the command:

```bash
pip install drf-spectacular
```

Add 'drf_spectacular' to your INSTALLED_APPS in settings.py.

```python
INSTALLED_APPS = [
    ...
    'drf_spectacular',
]
```

Register the spectacular AutoSchema with DRF, by adding the following in the settings.py.

```python
REST_FRAMEWORK = {
    # YOUR SETTINGS
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
```

drf-spectacular ships with sane default settings that should work reasonably well out of the box. It is not necessary to specify any settings, but we recommend to specify at least some metadata.

```python
SPECTACULAR_SETTINGS = {
    'TITLE': 'Your Project API',
    'DESCRIPTION': 'Your project description',
    'VERSION': os.environ.get('GIT_TAG', 'dev'),
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}
```

## Generate your schema with the CLI:

```bash
./manage.py spectacular --color --file schema.yml
```

## Create the endpoints for the schema

In the urls.py file specific for the app, using the path, direct the traffic to your view function.
Add the following code

```python
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    ...,
    # API Schema:
    path("api/", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),

]
```

Start the server and navigate to

http://127.0.0.1:8000/api/schema/ - to download the yml file

http://127.0.0.1:8000/api/schema/swagger-ui/ - to check out the GUI

http://127.0.0.1:8000/api/schema/redoc/ - for the reference documentation

# Useful Links

- https://www.django-rest-framework.org/

- https://pypi.org/project/djangorestframework/
- https://pypi.org/project/drf-spectacular/

- https://www.openapis.org/what-is-openapi
- https://swagger.io/blog/api-development/redoc-openapi-powered-documentation/
