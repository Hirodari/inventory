"""
    Test the validator functions
    command line: python -m pytest test/unit/test_validator.py
"""

from app.utils.validators import validate_integer
import pytest


class TestIntegerValidator:
    def test_valid(self):
        validate_integer("int_arg", 10, 0, 20, "cust min msg", "cust max msg")

    def test_type_error(self):
        with pytest.raises(TypeError):
            validate_integer("int_arg", 10.5, 0, 20, "cust min msg", "cust max msg")

    def test_min_std_err_msg(self):
        with pytest.raises(ValueError) as ex:
            validate_integer("arg", 10, 20, 30)
            assert "arg" in str(ex.value)
            assert "20" in str(ex.value)

    def test_min_custom_err_msg(self):
        with pytest.raises(ValueError) as ex:
            validate_integer("int_arg", 5, 10, 20, custom_min_message="custom")
            assert str(ex.value) == "custom"

    def test_max_std_err_msg(self):
        with pytest.raises(ValueError) as ex:
            validate_integer("int_arg", 30, 0, 20)
            assert "int_arg" in str(ex.value)
            assert "20" in str(ex.value)

    def test_max_custom_err_msg(self):
        with pytest.raises(ValueError) as ex:
            validate_integer("int_arg", 30, 0, 20, custom_max_message="custom")
            assert str(ex.value) == "custom"
