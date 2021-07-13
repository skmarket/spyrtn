from spyrtan.Chapter4.section1.quiz import (
    quiz1,
    quiz2
)


def test_section1_1():
    assert quiz1() == (2304 * 2.5 + 2239 * 1.2) / 5


def test_section1_2():
    assert quiz2() == 2 or quiz2() == 2.