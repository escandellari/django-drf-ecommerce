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
