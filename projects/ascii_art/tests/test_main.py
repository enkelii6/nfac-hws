import pytest

from projects.ascii_art.justify.justify import justify


def test_justify():
    with pytest.raises(ValueError):
        justify('asd', 'asd')
