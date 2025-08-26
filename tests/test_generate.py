from src.app.services import generate

import pytest

def test_numbers():
    assert len(generate.get_numbers(0)) == 0
    assert len(generate.get_numbers(1)) == 1
    assert len(generate.get_numbers(11)) == 11

def test_backup():
    assert len(generate.get_backup(0)) == 0
    assert len(generate.get_backup(1)) == 1
    assert len(generate.get_backup(11)) == 11


def test_raises_type():
    ...

def test_raises_value():
    ...
