from src.app.services import validate

import pytest


def test_level_raises_invalid():
    with pytest.raises(
        ValueError, 
        match='Numerical value is required'
    ):
        validate.validate_level('one')

def test_level_raises_low():
    with pytest.raises(
        ValueError, 
        match='Value must be greater than 0'
    ):
        validate.validate_level(-1)

def test_level_raises_high():
    with pytest.raises(
        ValueError, 
        match='Value must be less than 5'
    ):
        validate.validate_level(5)


def test_guess_raises_invalid():
    with pytest.raises(
        ValueError,
        match='No input'
    ):
        validate.validate_guess(None, 4)

def test_guess_raises_low():
    with pytest.raises(
        ValueError,
        match='Insufficient values'
    ):
        validate.validate_guess((1, 2, 3), 4)

def test_guess_raises_low():
    with pytest.raises(
        ValueError,
        match='Too many values'
    ):
        validate.validate_guess((1, 2, 3, 4, 5), 4)


def test_part_raises_invalid():
    with pytest.raises(
        ValueError,
        match='All values must be between 0 and 7'
    ):
        validate.validate_part('number')


def test_part_raises_low():
    with pytest.raises(
        ValueError,
        match='All values must be between 0 and 7'
    ):
        validate.validate_part(-1)

def test_part_raises_high():
    with pytest.raises(
        ValueError,
        match='All values must be between 0 and 7'
    ):
        validate.validate_part(8)


def test_extend_raises():
    ...

def test_sql_raises():
    ...
