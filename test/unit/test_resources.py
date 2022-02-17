"""
    Test for resource class
"""
from app.models.inventory import Resources
import pytest


class TestResourceClass:
    @pytest.fixture
    def resource_values(self):
        return {
            "name": "name_test",
            "manufacturer": "manu_name",
            "total": 10,
            "allocated": 5
        }

    @pytest.fixture
    def resource(self, resource_values):
        return Resources(**resource_values)

    def test_create_resource(self, resource_values, resource):
        for attr_name in resource_values:
            assert getattr(resource, attr_name) == resource_values.get(attr_name)

    def test_invalid_total_type(self):
        with pytest.raises(TypeError):
            Resources("name_test", "manu_name", 10.5, 5)

    def test_invalid_total_value(self):
        with pytest.raises(ValueError):
            Resources("name_test", "manu_name", -2, 5)

    @pytest.mark.parametrize('total,allocated', [(10, -5), (10, 20)])
    def test_invalid_allocated_value(self, total, allocated):
        with pytest.raises(ValueError):
            Resources("name_test", "manu_name", total, allocated)

    def test_category(self, resource):
        assert resource.category == "resources"

    def test_available(self, resource):
        assert resource.available == resource.total - resource.available

    def test_str(self, resource):
        assert str(resource) == resource._name

    def test_repr(self, resource):
        assert repr(resource) == 'Resources(name_test, manu_name, total=10,allocated=5)'
        
    def test_claim(self, resource):
        n = 2
        original_total = resource.total
        original_allocation = resource.allocated
        resource.claim(n)
        assert resource.total == original_total
        assert resource.allocated == original_allocation + n

    @pytest.mark.parametrize("value", [-1, 0, 1_000])
    def test_invalid_claim(self, resource, value):
        with pytest.raises(ValueError):
            resource.claim(value)

    def test_freeup(self, resource):
        n = 2
        original_allocation = resource.allocated
        resource.freeup(n)
        assert resource._allocated == original_allocation - n

    @pytest.mark.parametrize("value", [-1, 0, 1_000])
    def test_invalid_freeup(self, resource, value):
        with pytest.raises(ValueError):
            resource.freeup(value)

    def test_died(self, resource):
        n = 2
        original_total = resource._total
        original_allocated = resource._allocated
        resource.died(n)
        assert resource._total == original_total - n
        assert resource._allocated == original_allocated - n

    @pytest.mark.parametrize("value", [-1, 0, 1_000])
    def test_invalid_died(self, resource, value):
        with pytest.raises(ValueError):
            resource.died(value)

    def test_purchased(self, resource):
        n = 2
        original_total = resource._total
        resource.purchased(n)
        assert resource.total == original_total + n

    @pytest.mark.parametrize("value", [-1, 0])
    def test_invalid_purchase(self, resource, value):
        with pytest.raises(ValueError):
            resource.purchased(value)
