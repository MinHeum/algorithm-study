import re

answer = []
S = input() # 문자열을 입력받는다.

def reverse_string(input_string):
    ret = ""
    for i in input_string.split():
        ret += "".join(reversed(i))
        ret += " "
    return ret.rstrip()

pattern = re.compile("(<.+?>)|([^<>]+)") # 정규표현식 사용
arr = re.split(pattern, S)               # 패턴에 맞게 split한 배열을 선언

for word in arr:
    if word == "" or word is None:
        continue
    if "<" in word:
        answer.append(word) # "<"를 포함한 word는 그냥 정답배열에 넣는다
    else:
        answer.append(reverse_string(word)) # 이외의 word는 뒤집어서 넣는다.

for i in answer:
    print(i, end="")
