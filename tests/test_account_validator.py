import pytest
from lib.account_validator import AccountParametersValidator

def test_is_username_valid():
    validator = AccountParametersValidator("mike10", "mike@yahoo.com", "Ilovegab123")
    assert validator.is_username_valid() == True


def test_is_username_invalid():
    validator = AccountParametersValidator("", "mike@yahoo.com", "Ilovegab123")
    assert validator.is_username_valid() == False

def test_is_email_valid():
    validator = AccountParametersValidator("mike10", "mike@yahoo.com", "Ilovegab123")
    assert validator.is_email_valid() == True

def test_is_email_invalid():
    validator = AccountParametersValidator("mike10", "mikeyahoo.com", "Ilovegab123")
    assert validator.is_email_valid() == False

def test_is_password_invalid():
    validator = AccountParametersValidator("mike10", "mikeyahoo.com", "Ilovegab123")
    assert validator.is_user_password_valid() == False

def test_is_password_valid():
    validator = AccountParametersValidator("mike10", "mikeyahoo.com", "Ilovegab123!")
    assert validator.is_user_password_valid() == True

def test_is_valid():
    validator = AccountParametersValidator("mike10", "mike@yahoo.com", "Ilovegab123!")
    assert validator.is_valid() == True

def test_not_valid():
    validator_1 = AccountParametersValidator("mike10", "mikeyahoo.com", "Ilovegab123")
    assert validator_1.is_valid() == False
    validator_2 = AccountParametersValidator(None, "mikeyahoo.com", "Ilovegab123")
    assert validator_2.is_valid() == False


def test_generate_errors():
    validator_1 = AccountParametersValidator("mike10", "mikeyahoo.com", "Ilovegab123")
    assert validator_1.generate_errors() == ["You must enter a valid email", "Password must have at least 8 characters, include a letter, number and special character"]

def test_get_valid_title_refuses_if_invalid():
    validator_1 = AccountParametersValidator("mike10", "mikeyahoo.com", "Ilovegab123!")
    with pytest.raises(ValueError) as err:
        validator_1.get_valid_email()
    assert str(err.value) == "Cannot get valid email"

