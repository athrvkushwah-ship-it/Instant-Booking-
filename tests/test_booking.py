import pytest

from booking import validate_movie, validate_quantity


# Test 1: Check whether a valid movie is accepted

def test_valid_movie():

    result = validate_movie("Goolmal 1")

    assert result == True


# Test 2: Check whether an invalid movie is rejected

def test_invalid_movie():

    result = validate_movie("Avengers")

    assert result == False


# Test 3: Check whether a valid ticket quantity is accepted

def test_valid_quantity():

    result = validate_quantity(3)

    assert result == True


# Test 4: Check whether zero tickets are rejected

def test_invalid_quantity():

    result = validate_quantity(0)

    assert result == False