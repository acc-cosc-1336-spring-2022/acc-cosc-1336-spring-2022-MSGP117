import decisions

#num = int(input('Enter a number: '))
#if decisions.is_even(num):
    #7print(num, 'is_even')
#else:
    #print(num, 'is odd')

#num = int(input('Enter a grade: '))
#print(decisions.get_letter_grade(num)) #module

#min = 1
#max = 10 #variables
#num = int(input('Enter a number: '))
#result = decisions.number_is_in_range_and(min, max, num)
#if(result):
 #   print(num, 'is in range')
#else:
 #   print(num, 'is not in range')

letter = input('Enter a letter: ')
result = decisions.is_letter_consonant(letter)
if(result):
    print(letter, "is consonant")
else:
    print(letter, "is vowel")