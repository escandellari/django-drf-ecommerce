# SETUP

- python3 -m venv .venv
- source .venv/bin/activate
- pip install django
- django-admin startproject <projectname>
  - By adding a full stop at the end, it will create the project without any subfolders

## Packages

- django
- djangorestframework
- python-dotenv
- pytest
- pytest-django
- black
- flake8
- django-mptt
- drf-spectacular

## Splitting settings into dev and prod

- Create settings folder
- Move settings.py into settings folder
- Rename to base.py
- Create a dev.py and prod.py files
- Add the following line to both files: `from .base import *`
- Change the manage.py file to use either files depending on the DEBUG flag

```python
    if base.DEBUG:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drfecommerce.settings.development")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drfecommerce.settings.production")
```

## Secret Key Generation

```bash
python manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Once you have the key, copy it into the base.py file

## Pytest

- pip install pytest
- pip install pytest-django
- Add pytest.ini file and add the following

```ini
[pytest]
DJANGO_SETTINGS_MODULE = drfecommerce.settings.development
python_files = test_*
```

- Create a folder called tests
- Add test files, with prefix `test_`
- Run the test with `pytest`

# Create an APP within a specific folder

Run the following to create an app

```bash
./manage.py startapp <product_name> <folder>
```

Example:

```bash
./manage.py startapp product ./drfecommerce/product
```

## Add it to the settings

In the base settings, add the <product_name> as specified above.

If created in a specific folder, then it would be <folder>.<product_name>

Example:

```python
"drfecommerce.product",
```

In the apps.py file define the same in the name

# DRF SPECTACULAR

pip install drf-spectacular

- Create serializer for all the endpoints
- Create views using ViewSets
- Register the ViewSets within the urls
- Add the following to the urlpatterns

```python
    path("api/", include(router.urls)),
    path("api/schema", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/docs", SpectacularSwaggerView.as_view(url_name="schema")),
```

- Run the following to create the schema

```bash
    ./manage.py spectacular --color --file schema.yml
```
