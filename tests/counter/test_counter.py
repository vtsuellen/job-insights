from src.pre_built.counter import count_ocurrences

PATH = "data/jobs.csv"


def test_counter():
    assert count_ocurrences(PATH, "Python") == 1639
    assert count_ocurrences(PATH, "Javascript") == 122
