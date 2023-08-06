arr1 = [0] * 26
arr2 = [0] * 26

word_a = input()
word_b = input()

for i in word_a:
    arr1[ord(i)-97] += 1

for i in word_b:
    arr2[ord(i)-97] += 1

for i in range(0,26):
    arr1[i] = arr1[i] - arr2[i]

result = 0

for i in range(0,26):
    result += abs(arr1[i])

print(result)
