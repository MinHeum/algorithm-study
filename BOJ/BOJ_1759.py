from itertools import combinations

L, C = map(int, input().split())
lst = input().split()

vowels = ["a", "e", "i", "o", "u"]
lst_vowel = [i for i in lst if i in vowels]
lst_consonant = [i for i in lst if i not in vowels]

answer = []

# 최소 한 개의 모음과 최소 두 개의 자음으로 구성된 조합을 생성
for i in range(1, L - 1):
    for vowel_comb in combinations(lst_vowel, i):
        consonant_comb = combinations(lst_consonant, L - i)
        for consonant in consonant_comb:
            s = "".join(sorted(vowel_comb + consonant))
            answer.append(s)

answer.sort()
for e in answer:
    print(e)
