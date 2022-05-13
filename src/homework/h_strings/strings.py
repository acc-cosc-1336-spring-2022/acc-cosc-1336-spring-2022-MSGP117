def get_hamming_distance(DNA1, DNA2):
    distance = 0
    L = len(DNA1)
    for i in range (L):
        if DNA1[i] != DNA2[i]:
            distance += 1
    return distance

#ex_dist = get_hamming_distance("GATTACA", "GACTATA")
#print(ex_dist)

def reversed_dna(dna):
    reversedna = ""
    index = len(dna)
    while index > 0:
        reversedna += dna[ index - 1 ]
        index = index - 1
    return reversedna

def dna_complement(s):
    str1 = ''
    for letter in s:
        str1 += letter
    return str1

def get_dna_complement(DNA):
    reversed = reversed_dna(DNA)
    newreverse = list(reversed)
    for i in range(10):
        if newreverse[i] == 'T':
            newreverse[i] = 'A'
        elif newreverse[i] == 'A':
            newreverse[i] = 'T'
        elif newreverse[i] == 'G':
            newreverse[i] = 'C'
        elif newreverse[i] == 'C':
            newreverse[i] = 'G'
            i += 1

    new_reverse = dna_complement(newreverse)

    return new_reverse
