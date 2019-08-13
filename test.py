import pytest
from main import verify_input

def test_input_contains_only_roman_number():
    assert verify_input("IVXLCDM") == "IVXLCDM"

def test_wrong_input_calls_for_error():
    with pytest.raises(ValueError, match="This is not a correct roman number"):
        verify_input("AIV")
