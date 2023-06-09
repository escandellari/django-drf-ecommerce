import json

import pytest

# Give access to the DB
pytestmark = pytest.mark.django_db


class TestCategoryEndpoint:
    endpoint = "/api/category/"

    # def test_category_get(self, category_factory, api_client):
    #     # ARRANGE - Initialise the factory, by adding data to the testing db
    #     category_factory()
    #     # ACT
    #     response = api_client().get(self.endpoint)
    #     # ASSERT
    #     assert response.status_code == 200

    def test_category_get_batch(self, category_factory, api_client):
        # ARRANGE - Initialise the factory, by adding data to the testing db
        category_factory.create_batch(4)
        # ACT
        response = api_client().get(self.endpoint)
        print(json.loads(response.content))
        # ASSERT
        assert len(json.loads(response.content)) == 4


class TestBrandEndpoint:
    endpoint = "/api/brand/"

    def test_brand_get(self, brand_factory, api_client):
        # ARRANGE - Initialise the factory, by adding data to the testing db
        brand_factory()
        # ACT
        response = api_client().get(self.endpoint)
        # ASSERT
        assert response.status_code == 200


class TestProductEndpoint:
    endpoint = "/api/product/"

    def test_product_get(self, product_factory, api_client):
        # ARRANGE - Initialise the factory, by adding data to the testing db
        product_factory()
        # ACT
        response = api_client().get(self.endpoint)
        # ASSERT
        assert response.status_code == 200
