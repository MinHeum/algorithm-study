N = input()
words = [input() for _ in range(int(N))]    

# words의 원본
original = words[:]

# words의 순서를 유지하며 중복을 제거
words = list(dict.fromkeys(words))

words.sort(key=lambda x: x[0])

max_len = -1

word_a = ''
word_b = ''

def compare(a, b):
    cnt = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            cnt += 1
        else:
            break
    return cnt


# words에서 인접한 두 단어를 비교하여 공통된 길이를 계산한다.
for i in range(len(words)-1):
    cnt = compare(words[i], words[i+1])
    if cnt > max_len:
        max_len = cnt
        word_a = words[i]
        word_b = words[i+1]

# original에서 word_a 와 word_b의 인덱스를 찾는다.
idx_a = original.index(word_a)
idx_b = original.index(word_b)

# 인덱스가 더 작은 단어를 먼저 출력한다.
if idx_a < idx_b:
    print(word_a)
    print(word_b)

else:
    print(word_b)
    print(word_a)