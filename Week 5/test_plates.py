""" Problem:
In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below,
wherein is_valid still expects a str as input and returns True if that str meets all requirements and False if it
does not, but main is only called if the value of __name__ is "__main__":
def main():
    ...


def is_valid(s):
    ...


if __name__ == "__main__":
    main()
Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation
of is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_plates.py """


import pytest
from plates import is_valid

# Test if the function validates plates with fewer than 2 characters or more than 6 characters
def test_length_validation():
    assert not is_valid("A")  # Too short
    assert not is_valid("ABCDEFG")  # Too long

# Test if the function handles plates that do not start with two letters
def test_start_with_letters():
    assert not is_valid("1ABCD")  # Starts with a number
    assert not is_valid("A1BCD")  # Does not start with two letters

# Test if the function handles plates with numbers in the middle
def test_numbers_in_middle():
    assert not is_valid("AA1A22")  # Number in the middle
    assert is_valid("AA1222")  # Numbers at the end

# Test if the function handles plates with the first number being '0'
def test_zero_as_first_number():
    assert not is_valid("AA0123")  # First number is 0
    assert is_valid("AA1023")  # First number is not 0

# Test if the function handles plates with invalid characters (non-alphanumeric)
def test_invalid_characters():
    assert not is_valid("AA-123")  # Contains a hyphen
    assert not is_valid("AA?123")  # Contains a question mark

# Test valid plates
def test_valid_plates():
    assert is_valid("AA123")  # Valid plate
    assert is_valid("AB12")   # Valid plate

# Test if the function correctly handles edge case of exactly two letters (minimum valid length)
def test_minimum_valid_length():
    assert is_valid("AB")  # Minimum valid length
