from src.app.services import stats

import pytest


def test_score():
    assert stats.score_code((1, 2, 3, 4), (1, 2, 3, 4), 4) == 0
    assert stats.score_code((1, 2, 3, 4, 5), (1, 2, 3, 4, 5), 5) == 0
    assert stats.score_code((0, 0, 3, 4), (1, 2, 3, 4), 4) == 5
    assert stats.score_code((0, 0, 0, 0, 0), (1, 2, 3, 4, 5), 5) == 10
    assert stats.score_code((0, 0, 0, 0), (1, 2, 3, 4), 4) == 10


def test_no_guess():
    with pytest.raises(
        TypeError,
        match='No guess provided'
    ):
        stats.score_code(None, (1, 2, 3, 4), 4)

def test_invalid_guess():
    with pytest.raises(
        ValueError,
        match='Guess and code must be the same length'
    ):
        stats.score_code((1, 2, 3), (1, 2, 3, 4), 4)

def test_no_code():
    with pytest.raises(
        TypeError,
        match='No code provided'
    ):
        stats.score_code((1, 2, 3, 4), None, 4)

def test_invalid_code():
    with pytest.raises(
        ValueError,
        match='Guess and code must be the same length'
    ):
        stats.score_code((1, 2, 3, 4), (1, 2, 3), 4)

def test_no_level():
    with pytest.raises(
        TypeError,
        match='No level provided'
    ):
        stats.score_code((1, 2, 3, 4), (1, 2, 3, 4), None)
