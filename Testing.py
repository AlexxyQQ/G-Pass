import pytest

"""Testing Login page"""
@pytest.fixture
def tester():
    """
    Getting User values and passing on
    """
    name = "Manjil"
    password = "Password123"
    return (name, password)


def test1(tester):
    """
    Testing for first name
    """
    first_name = "Manjil"
    assert tester[0] == first_name


def test_2(tester):
    """
    Testing Password
    """
    password_check = "Password"
    assert tester[1] == password_check

