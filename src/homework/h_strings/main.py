from strings import get_dna_complement, get_hamming_distance

def main():
    decision1 = str(input("Option 1 - Hamming Distance\t\nOption 2 - DNA Complement\t\nOption 3 - Exit\t"))
    if decision1 == '1':
        decision_1()
    elif decision1 == '2':
        decision_2()
    elif decision1 == '3':
        decision_3()
    
def decision_1():
    ham1 = input('Enter first DNA sequence: ')
    ham2 = input('Enter second DNA sequence: ')
    ham3 = get_hamming_distance(ham1, ham2)
    print('The hamming distance between DNA sequence one and DNA sequence two is ', ham3)
    new_decision = str(input('Would you like to enter a new DNA sequence? Y/N '))
    while new_decision == 'N':
        main()
    while new_decision == 'Y':
        decision_1()
        new_decision = str(input('Would you like to enter a new DNA sequence? Y/N '))

def decision_2():
    dna1 = input('Enter a DNA sequence: ')
    dna2 = get_dna_complement(dna1)
    print('The DNA compliment is ', dna2)
    decision = str(input('Would you like to enter a new DNA sequence? Y/N '))
    while decision.lower() == 'N':
        main()
    while decision.lower() == 'Y':
        decision_2()
        decision = str(input('Would you like to enter a new DNA sequence? Y/N '))

def decision_3():
    print('The program will end.')
    quit()

print('DNA Complement and Hamming Distance Test Program')
main()