from app.airport_data import is_valid_airport


def test_valid_airport():
    assert is_valid_airport("BLR") is True


def test_invalid_airport():
    assert is_valid_airport("XYZ") is False


def test_airport_code_case_sensitive():
    assert is_valid_airport("blr") is False