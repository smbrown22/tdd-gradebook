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
    return not letter_grade(score) == 'F'
def average(scores):
    if not isinstance(scores, list):
        raise TypeError("scores must be a list")
    if len(scores) == 0:
        raise ValueError
    if not all(isinstance(s, (int, float)) for s in scores): 
        raise TypeError("all scores must be numbers")
    return round(sum(scores) / len(scores), 2) 
def curved_score(score, bonus):
    if not isinstance(score , (int, float)) and not isinsance(bonus, (int, float)):
        raise TypeError("both score and bonus must be a number")

    if bonus < 0: 
        raise ValueError("bonus cannot be less than 0")
    
    if score + bonus > 100:
        return 100
    
    else:
        return score + bonus 