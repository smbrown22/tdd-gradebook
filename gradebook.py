def letter_grade(score):
    if not isinstance(score, (int, float)): 
        raise TypeError("score must be a number")
    
    if score >= 90:
        return 'A'
    elif score >= 80 and score < 90:
        return 'B'
    elif score >= 70 and score < 80:
        return 'C'
    elif score >= 60 and score < 70:
        return 'D'
    return 'F'
def is_passing(score):
    return not letter_grade == 'F'
def average(scores):
    pass
def curved_score(score, bonus):
    pass 