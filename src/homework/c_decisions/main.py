import decisions

print('Input Number for Options')
options = int(input())
print('Input Number for Total')
total = int(input())

result = decisions.get_options_ratio(options, total)

print(decisions.get_faculty_rating(result))