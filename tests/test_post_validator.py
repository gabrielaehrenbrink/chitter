import pytest
from lib.post_validator import PostParametersValidator

def test_is_valid():
    validator = PostParametersValidator("My content")
    assert validator.is_valid() == True

def test_not_valid():
    validator_1 = PostParametersValidator("")
    assert validator_1.is_valid() == False
    validator_2 = PostParametersValidator(None,)
    assert validator_2.is_valid() == False


def test_generate_errors():
    validator_1 = PostParametersValidator("")
    assert validator_1.generate_errors() == ["Content must not be blank"]

def test_get_valid_title_refuses_if_invalid():
    validator_1 = PostParametersValidator("")
    with pytest.raises(ValueError) as err:
        validator_1.get_valid_post_content()
    assert str(err.value) == "Cannot get valid content"


    
