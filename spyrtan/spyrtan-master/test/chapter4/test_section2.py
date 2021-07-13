from spyrtan.Chapter4.section2.quiz import (
    quiz2,
    quiz3
)

def test_section2_2():
    assert quiz2(0, 0) == 'draw'
    assert quiz2(0, 1) == 'win'
    assert quiz2(0, 2) == 'lose'
    assert quiz2(1, 0) == 'lose'
    assert quiz2(1, 1) == 'draw'
    assert quiz2(1, 2) == 'win'
    assert quiz2(2, 0) == 'win'
    assert quiz2(2, 1) == 'lose'
    assert quiz2(2, 2) == 'draw'


def test_section2_3():
    assert quiz2(0, 0, 0) == 'draw'
    assert quiz2(0, 0, 1) == 'win'
    assert quiz2(0, 0, 2) == 'lose'
    assert quiz2(0, 1, 0) == 'win'
    assert quiz2(0, 1, 1) == 'win'
    assert quiz2(0, 1, 2) == 'draw'
    assert quiz2(0, 2, 0) == 'lose'
    assert quiz2(0, 2, 1) == 'draw'
    assert quiz2(0, 2, 2) == 'lose'
    assert quiz2(1, 0, 0) == 'lose'
    assert quiz2(1, 0, 1) == 'lose'
    assert quiz2(1, 0, 2) == 'draw'
    assert quiz2(1, 1, 0) == 'lose'
    assert quiz2(1, 1, 1) == 'draw'
    assert quiz2(1, 1, 2) == 'win'
    assert quiz2(1, 2, 0) == 'draw'
    assert quiz2(1, 2, 1) == 'win'
    assert quiz2(1, 2, 2) == 'win'
    assert quiz2(2, 0, 0) == 'win'
    assert quiz2(2, 0, 1) == 'draw'
    assert quiz2(2, 0, 2) == 'win'
    assert quiz2(2, 1, 0) == 'draw'
    assert quiz2(2, 1, 1) == 'lose'
    assert quiz2(2, 1, 2) == 'lose'
    assert quiz2(2, 2, 0) == 'win'
    assert quiz2(2, 2, 1) == 'lose'
    assert quiz2(2, 2, 2) == 'draw'
    