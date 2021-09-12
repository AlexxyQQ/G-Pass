

import pytest
@pytest.fixture()
def insert_test():
    first_name = 'shreeti'
    last_name = 'ranjit'
    age = 19
    gender = 'female'
    contact_number = 9840000000
    return [first_name,last_name,age,gender,contact_number]
def insert_test1(insert_test):
    first_name1 = 'shreeti'
    assert insert_test[0] == first_name1
def insert_test2(insert_test):
    last_name1 = 'ranjit'
    assert insert_test[1] == last_name1
def insert_test3(insert_test):
    age1 = 19
    assert insert_test[2] == age1
def insert_test4(insert_test):
    gender1 = 'Female'
    assert insert_test[3] == gender1
def insert_test5(insert_test):
    contact_number1 = 9840000000
    assert insert_test[4] == contact_number1


