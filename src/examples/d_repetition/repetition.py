def test_config():
    return True

def display_numbers(num):
    cnt = 0
    while cnt < num:
        print(cnt + 1)
        cnt = cnt + 1 #statement that makes the cnt < num = False

def sum_of_squares(num):
    cnt = 0
    sum = 0
    while cnt < num:
            sum = sum * cnt
            cnt = cnt + 1  #statement that makes boolean expression false
        
    return sum

def prompt_user():
    keep_going = 'y'

    while keep_going == 'y':
        keep_going = input("loop again, type y")

def for_intro_loop():
    for num in [1,2,3,4,5]:
        print(num)

def for_intro_loop_strings():
    for name in ['winken', 'blinken', 'Nod']:
        print(name)

def for_num_in_range(val):
    for num in range(val):
        print(num, "Hello World")

def for_num_in_range_w_start_value(num, num1):
    for val in range(num, num1):
        print(val)

def for_num_range_w_step_value(num, num1, num2):
    for val in range(num, num1, num2):
        print(val)

def for_display_sum_of_squares(num, num1):
    for val in range(num, num1):
        square = val ** 2
        print(val, '\t', square)