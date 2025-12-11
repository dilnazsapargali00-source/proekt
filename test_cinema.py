import pytest
from cinema import CinemaStatistics

def test_add_movie():
    c = CinemaStatistics()
    c.add_movie("Test", "Action", 100, 8.5)
    assert len(c.movies) == 1

def test_negative_views_error():
    c = CinemaStatistics()
    with pytest.raises(ValueError):
        c.add_movie("Bad Film", "Drama", -10, 5)
