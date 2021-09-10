import pytest
import random

@pytest.fixture
def tester():
    email="eggplant@yahoo.com"
    n_pass="Qwerty1234"
    n_passcheck="Qwerty1234"
    return (email,n_pass,n_passcheck)


def test1(tester):
    first_name = "eggplant@yahoo.com"
    assert tester[0] == first_name


def test_2(tester):
    password_check = "Qwerty1234"
    assert tester[1] == password_check


def test_3(tester):
    password_check2 = "Qwerty1234"
    assert tester[2] == password_check2

