import pytest
from gradebook import letter_grade, is_passing, average, curved_score 

def test_letter_grade_A():
    assert letter_grade(95) == 'A' 

def test_letter_grade_F():
    assert letter_grade(45) == 'F' 

@pytest.mark.parametrize("score, expected", [(90, 'A'), (45, 'F')])
def test_letter_grade(score, expected):
    assert letter_grade(score) == expected

def test_letter_grade_invalid_type():
    with pytest.raises(TypeError):
        letter_grade("hello")

def test_is_passing_true():
    assert is_passing(75) == True

def test_is_passing_false():
    assert is_passing(45) == False

def test_is_passing_invalid_type():
    with pytest.raises(TypeError):
        is_passing("hello")

def test_average_correct():
    assert average([80, 90, 100]) == 90.0

def test_average_empty():
    with pytest.raises(ValueError): 
        average([]) 

def test_average_not_list():
    with pytest.raises(TypeError):
        average("not a list")

def test_average_bad_items():
    with pytest.raises(TypeError):
        average(["this is a list" , 'not the right kind of list', 90])

def test_curved_score_true():
    assert curved_score(75, 10) == 85

def test_curved_score_too_high():
    assert curved_score(98, 10) == 100
    
