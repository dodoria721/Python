# 딕셔너리를 사용한 풀이

n = int(input())
dna = list(input())

conversions = {
    'AA': 'A',
    'AC': 'A',
    'GT': 'A',
    'CA': 'A',
    'TG': 'A',
    'AG': 'C',
    'GA': 'C',
    'CC': 'C',
    'AT': 'G',
    'GG': 'G',
    'CT': 'G',
    'TA': 'G',
    'TC': 'G',
    'GC': 'T',
    'CG': 'T',
    'TT': 'T'
}

for x in range(n - 1, 0, -1):
    substr = ''.join(dna[x - 1:x + 1])
    if substr in conversions:
        dna[x - 1:] = conversions[substr]

print(''.join(dna))

# 리스트를 사용한 풀이
n = int(input())
dna =list(input())

for x in range(n-1, 0, -1):
    if dna[x-1:] in [['A', 'A'],['A','C'],['G','T'],['C','A'],['T','G']]: # A
        dna[x-1:] = 'A'

    elif dna[x-1:] in [['A', 'G'],['G','A'],['C','C']]: # C
        dna[x-1:] = 'C'

    elif dna[x-1:] in [['A', 'T'], ['G', 'G'],['C','T'],['T','A'],['T','C']]: # G
        dna[x-1:] = 'G'

    elif dna[x-1:] in [['G','C'], ['C','G'], ['T','T']]: # T
        dna[x-1:] = 'T'

print(''.join(dna))