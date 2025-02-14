import pytest
from user_registration import (
    validate_first_name,
    validate_last_name,
    validate_email,
    validate_contact_number,
    validate_password
)

# first name validation
@pytest.mark.parametrize("first_name, expected", [
    ("Yash", True),
    ("yo", False),
    ("yash", False),
    ("Y", False)
])
def test_validate_first_name(first_name, expected):
    assert validate_first_name(first_name) == expected, f"validation faild for name : {first_name}"

# last name validation
@pytest.mark.parametrize("last_name, expected", [
    ("Goy", True),
    ("goyal", False),
    ("G", False),
    ("go", False)
])
def test_validate_last_name(last_name, expected):
    assert validate_last_name(last_name) == expected

# email validation
@pytest.mark.parametrize("email, expected", [
    ("test@example.com", True),
    ("test.email@example.com", True),
    ("test@.com", False),
    ("@example.com", False)
])
def test_validate_email(email, expected):
    assert validate_email(email) == expected

# phone number validation
@pytest.mark.parametrize("phone_number, expected", [
    ("91 9876543210", True),
    ("1234 9876543210", False),
    ("324 9865356934", True),
    ("9876543210", False),
    ("+91 9876543210", False)
])
def test_validate_contact_number(phone_number, expected):
    assert validate_contact_number(phone_number) == expected

# password validation
@pytest.mark.parametrize("password, expected", [
    ("Pass@123", True),
    ("pass#word", False),
    ("PASS#&1234@", True),
    ("Pass123", False)
])

def test_validate_password(password, expected):
    assert validate_password(password) == expected