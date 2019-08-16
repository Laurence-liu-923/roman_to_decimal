import pytest
from main import verify_input, convert_roman_to_decimal
from decimal_roman_table import decimal_roman_table

def test_input_contains_only_roman_number():
    assert verify_input("IVXLCDM") == "IVXLCDM"

def test_wrong_input_calls_for_error():
    with pytest.raises(ValueError, match="This is not a correct roman number"):
        verify_input("AIV")

@pytest.mark.parametrize("expected,test_input", decimal_roman_table)
def test_convert_roman_to_decimal(test_input, expected):
        assert convert_roman_to_decimal(test_input) == expected

