"""
    Test for CPU class
"""

from app.models.hardware import CPU
import pytest


class TestCPUClass:
    @pytest.fixture
    def cpu_values(self):
        return {
            "name": "CPU TEST",
            "manufacturer": " Intel",
            "total": 10,
            "allocated": 5,
            "cores": 26,
            "socket": "socket.app",
            "power_watts": 20
        }

    @pytest.fixture
    def cpu_func(self, cpu_values):
        return CPU(**cpu_values)

    def test_cpu_properties(self, cpu_func, cpu_values):
        for attr_name in cpu_values:
            assert getattr(cpu_func, attr_name) == cpu_values.get(attr_name)

    @pytest.mark.parametrize(
        "cores, exception", [(10.5, TypeError),
        (-1, ValueError), (0, ValueError)])
    def test_create_invalid_core(self, cores, exception, cpu_values):
        cpu_values["cores"] = cores
        with pytest.raises(exception):
            CPU(**cpu_values)

    @pytest.mark.parametrize(
        "pw, exception",
        [(10.5, TypeError), (-1, ValueError), (0, ValueError)])
    def test_create_invalid_pw_value(self, pw, exception, cpu_values):
        cpu_values["power_watts"] = pw
        with pytest.raises(exception):
            CPU(**cpu_values)

    def test_cpu_repr(self, cpu_func):
        assert cpu_func.category in repr(cpu_func)
        assert cpu_func.name in repr(cpu_func)
        assert cpu_func.socket in repr(cpu_func)
        assert str(cpu_func.cores) in repr(cpu_func)
