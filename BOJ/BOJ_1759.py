from sys import stdin
import itertools

L, C = map(int,stdin.readline().split())
lst = list(stdin.readline().split())

# 최소 한개의 모음 (a,e,i,o,u) 와 최소 두 개의 자음으로 구성
lst_vowel = []
lst_consonant = []
for i in lst:
    if i in ['a','e','i','o','u']:
        lst_vowel.append(i)
    else:
        lst_consonant.append(i)

answer = []
for i in range(1, len(lst_vowel)+1):
    for vowel in itertools.combinations(lst_vowel, i):
        for consonant in itertools.combinations(lst_consonant, L-len(vowel)):
            if len(consonant) >= 2: 
                s = sorted(''.join(vowel+consonant))
                answer.append(s)
answer.sort()
for e in answer:
    print(''.join(e))
