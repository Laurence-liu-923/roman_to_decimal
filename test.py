import pytest
from main import verify_input
from decimal_roman_table import decimal_roman_table
from converter import roman_to_decimal

def test_input_contains_only_roman_number():
    assert verify_input("IVXLCDM") == "IVXLCDM"

def test_wrong_input_calls_for_error():
    with pytest.raises(ValueError, match="This is not a correct roman number"):
        verify_input("AIV")

@pytest.mark.parametrize('decimal, roman', decimal_roman_table)

def test_converter(roman, decimal):
    assert roman_to_decimal(roman) == decimal