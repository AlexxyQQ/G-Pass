"""
Importing Pytest and random
"""
import pytest
import random


# Testing Password Changer

@pytest.fixture
def tester():
    email = "eggos@yahoo.com"
    n_pass = "Qwerty1234"
    n_passcheck = "Qwerty1234"
    return (email, n_pass, n_passcheck)

#Function with the parameter tester
def test1(tester):
    first_name = "eggos@yahoo.com"     #Testing for FirstName
    assert tester[0] == first_name


def test_2(tester):
    password_check = "Qwerty1234"    #Testing for New Password
    assert tester[1] == password_check


def test_3(tester):
    password_check2 = "Qwerty1234"     #Testing for reConfirmation
    assert tester[2] == password_check2
