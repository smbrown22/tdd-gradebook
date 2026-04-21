import pytest
from gradebook import letter_grade 

def test_letter_grade_A():
    assert letter_grade(95) == 'A' 

def test_letter_grade_F():
    assert letter_grade(55) == 'F' 

@pytest.mark.parametrize("score, expected", [(90, 'A'), (55, 'F')])
def test_letter_grade(score, expected):
    assert letter_grade(score) == expected