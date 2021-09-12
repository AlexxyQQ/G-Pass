"""
Importing random and pytest
"""
import pytest
import random

#Testing
@pytest.fixture
def tester():
    email = "eggplant@yahoo.com"
    old_pass = "Asdfg12345"
    new_pass = "Qwerty1234"
    new_passcheck = "Qwerty12345"
    return (email, old_pass, new_pass, new_passcheck)

#Function with the parameter tester
def test1(tester):
   email = "eggplant@yahoo.com"      #testing for email
    assert tester[0] == email


def test_2(tester):
    newpass = "Qwerty1234"             #testing for newPassword
    assert tester[2] == newpass


def test_3(tester):
    oldpass = "Qwerty1234"            # testing for old Password
    assert tester[1] == oldpass


def test_4(tester):
    newpasscheck = "Qwerty1234"
    assert tester[1] == newpasscheck
