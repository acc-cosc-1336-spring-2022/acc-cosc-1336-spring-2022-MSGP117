def test_config():
    return True

def get_letter_grade(grade):
    if grade >= 90 and grade <= 100:
        return 'A'
    elif grade >= 80 and grade < 90:
        return 'B'
    elif grade >= 70 and grade < 80:
        return 'C'
    elif grade >= 60 and grade < 70:
        return 'D'
    elif grade > 0 and grade <= 59:
        return 'F'
    elif grade < 0 and grade > 100:
        return 'Invalid Number'

def logical_op_precedence(op1, op2, op3):
    return not op1 and op2 or op3

def number_is_in_range_and(min, max, num):
    return num >= min and num <= max

def number_is_not_in_range(min, max, num):
    return not (num <= min and num >= max)

def num_is_not_in_range_or(min, max, num):
    return num < min or num > max

def is_letter_consonant(letter):
    return not (letter == 'a' or letter == 'e' or letter == 'o' or letter == 'u' or letter == '1')

