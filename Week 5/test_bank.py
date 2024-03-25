""" Problem:
In a file called bank.py, reimplement Home Federal Savings Bank from Problem Set 1, restructuring your code per the below,
wherein value expects a str as input and returns an int, namely 0 if that str starts with “hello”, 20 if that str starts
with an “h” (but not “hello”), or 100 otherwise, treating the str case-insensitively. You can assume that the string passed
to the value function will not contain any leading spaces. Only main should call print.

def main():
    ...


def value(greeting):
    ...


if __name__ == "__main__":
    main()
Then, in a file called test_bank.py, implement three or more functions that collectively test your implementation of value thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_bank.py """


import pytest
from bank import value

# Test function to check if the greeting starts with "hello" (case insensitive).
def test_value_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO there") == 0

# Test function to check if the greeting starts with "h" but not "hello" (case insensitive).
def test_value_h():
    assert value("hi") == 20
    assert value("Hi there") == 20
    assert value("hey") == 20
    assert value("H") == 20

# Test function to check if the greeting does not start with "h" or "hello" (case insensitive).
def test_value_other():
    assert value("good morning") == 100
    assert value("Good evening") == 100
    assert value("yes") == 100

# Test function to check if the function handles empty strings correctly.
def test_value_empty():
    assert value("") == 100
