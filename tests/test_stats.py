from src.app.services.db.guesses import reset
from src.app.services import stats

import pytest


def test_score():
    assert stats.score_code((1, 2, 3, 4), (1, 2, 3, 4), 4) == 0
    assert stats.score_code((1, 2, 3, 4, 5), (1, 2, 3, 4, 5), 5) == 0
    assert stats.score_code((0, 0, 3, 4), (1, 2, 3, 4), 4) == 5
    assert stats.score_code((0, 0, 0, 0, 0), (1, 2, 3, 4, 5), 5) == 10
    assert stats.score_code((0, 0, 0, 0), (1, 2, 3, 4), 4) == 10
    reset()


def test_invalid():
    ...
