"""
 Testing Capacity base class
"""

from app.models.hardware import Storage, HDD, SSD
import pytest


@pytest.fixture
def storage_values():
    return {
        "name": "Storage TEST",
        "manufacturer": " Intel",
        "total": 10,
        "allocated": 5,
        "capacity_gb": 26
    }


@pytest.fixture
def storage(storage_values):
    return Storage(**storage_values)


def test_create_storage(storage, storage_values):
    for attr_name in storage_values:
        assert getattr(storage, attr_name) == storage_values.get(attr_name)


@pytest.mark.parametrize(
    "capacity, exception",
    [(10.5, TypeError), (-1, ValueError), (0, ValueError)])
def test_invalid_size(capacity, exception, storage_values):
    storage_values["capacity_gb"] = capacity
    with pytest.raises(exception):
        Storage(**storage_values)


def test_capacity_property(storage):
    assert storage.capacity_gb == storage._capacity_gb


def test_repr(storage):
    assert storage.category in repr(storage)
    assert str(storage.capacity_gb) in repr(storage)

# Testing module for HDD storage

@pytest.fixture
def hdd_values():
    return {
        "name": "HDD TEST",
        "manufacturer": " Intel",
        "total": 10,
        "allocated": 5,
        "capacity_gb": 26,
        "size": '2.5"',
        "rpm": 10_000
    }


@pytest.fixture
def hdd(hdd_values):
    return HDD(**hdd_values)


def test_create_hdd(hdd, hdd_values):
    for attr_name in hdd_values:
        assert getattr(hdd, attr_name) == hdd_values.get(attr_name)


@pytest.mark.parametrize("size, exception",
            [('1.0"', ValueError), (10, ValueError), ("test", ValueError)])
def test_invalid_size_hdd(size, exception, hdd_values):
    hdd_values['size'] = size
    with pytest.raises(exception):
        HDD(**hdd_values)


@pytest.mark.parametrize("rpm, exception", [(10.5, TypeError), (800, ValueError), (55_000, ValueError)])
def test_invalid_rpm(rpm, exception, hdd_values):
    hdd_values['rpm'] = rpm
    with pytest.raises(exception):
        HDD(**hdd_values)


def test_property_hdd(hdd):
    assert hdd.size == hdd._size
    assert hdd.rpm == hdd._rpm


def test_repr_hdd(hdd):
    assert hdd.category in repr(hdd)
    assert str(hdd.capacity_gb) in repr(hdd)
    assert hdd.size in repr(hdd)
    assert str(hdd.rpm) in repr(hdd)


@pytest.fixture
def ssd_values():
    return {
        "name": "SSD TEST",
        "manufacturer": " Intel",
        "total": 10,
        "allocated": 5,
        "capacity_gb": 26,
        "interface": "interface test"
    }


@pytest.fixture
def ssd(ssd_values):
    return SSD(**ssd_values)


def test_create_ssd(ssd, ssd_values):
    for attr_name in ssd_values:
        assert getattr(ssd, attr_name) == ssd_values.get(attr_name)


def test_interface_property_ssd(ssd):
    assert ssd.interface == ssd._interface


def test_repr_ssd(ssd):
    assert ssd.category in repr(ssd)
    assert str(ssd.capacity_gb) in repr(ssd)
    assert ssd.interface in repr(ssd)
