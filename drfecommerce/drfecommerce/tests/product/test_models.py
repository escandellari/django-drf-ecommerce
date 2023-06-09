import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_method(self, category_factory):
        # Arrange
        # Act
        category = category_factory(name="test category")
        # Assert
        assert category.__str__() == "test category"


class TestBrandModel:
    def test_str_method(self, brand_factory):
        brand = brand_factory(name="test brand")
        assert brand.__str__() == "test brand"


class TestProductModel:
    def test_str_method(self, product_factory):
        brand = product_factory(name="test product")
        assert brand.__str__() == "test product"
