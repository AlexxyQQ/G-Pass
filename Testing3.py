"""
Importing random and pytest
"""
import pytest
import random


@pytest.fixture
def tester():
    email = "eggplant@yahoo.com"
    old_pass = "Asdfg12345"
    new_pass = "Qwerty1234"
    new_passcheck = "Qwerty12345"
    return (email, old_pass, new_pass, new_passcheck)


def test1(tester):
   email = "eggplant@yahoo.com"
    assert tester[0] == email


def test_2(tester):
    newpass = "Qwerty1234"
    assert tester[2] == newpass


def test_3(tester):
    oldpass = "Qwerty1234"
    assert tester[1] == oldpass


def test_4(tester):
    newpasscheck = "Qwerty1234"
    assert tester[1] == newpasscheck
