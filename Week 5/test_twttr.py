import pytest
from twttr import shorten

# Test function to check if the shorten function removes all vowels from a string that contains only vowels.
def test_only_vowels():
    assert shorten("aeiou") == ""  # Test with lowercase vowels
    assert shorten("AEIOU") == ""  # Test with uppercase vowels

# Test function to verify that the shorten function returns the same string if there are no vowels to remove.
def test_no_vowels():
    assert shorten("bcdfg") == "bcdfg"  # Test with lowercase consonants
    assert shorten("BCDFG") == "BCDFG"  # Test with uppercase consonants

# Test function to check if the shorten function removes vowels from a string that contains a mix of vowels and consonants.
def test_mixed_characters():
    assert shorten("Hello, World!") == "Hll, Wrld!"  # Test with a common phrase
    assert shorten("Python Programming") == "Pythn Prgrmmng"  # Test with a mix of uppercase and lowercase letters

# Test function to ensure that the shorten function does not alter numbers or special characters.
def test_numbers_and_special_characters():
    assert shorten("12345!@#$%") == "12345!@#$%"  # Test with numbers and special characters

# Test function to verify that the shorten function handles an empty string correctly.
def test_empty_string():
    assert shorten("") == ""  # Test with an empty string
