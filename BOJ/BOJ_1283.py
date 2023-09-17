import sys

N = int(sys.stdin.readline())
used_letters = []  # 사용된 첫 글자 알파벳 리스트
for _ in range(N):
    input_word = list(map(str, sys.stdin.readline().split()))

    for idx in range(len(input_word)):
        # 현재 단어의 첫 글자가 사용된적 없는 알파벳이면
        if input_word[idx][0].upper() not in used_letters:
            used_letters.append(input_word[idx][0].upper())  # 사용된 알파벳으로 추가
            input_word[idx] = "[" + input_word[idx][0] + "]" + \
                input_word[idx][1:]  # 현재 단어의 첫 글자를 []로 감싼 후 출력
            print(" ".join(input_word))
            break

    else:
        for j in range(len(input_word)):
            letter_used = False  # 현재 단어의 알파벳을 사용했는지 여부
            for k in range(len(input_word[j])):
                # 현재 단어의 알파벳이 사용된 적 없는 알파벳이면
                if input_word[j][k].upper() not in used_letters:
                    used_letters.append(
                        input_word[j][k].upper())  # 사용된 알파벳으로 추가
                    letter_used = True
                    input_word[j] = input_word[j][:k] + "[" + input_word[j][k] + \
                        "]" + input_word[j][k +
                                            1:]  # 현재 단어의 첫 글자를 []로 감싼 후 출력
                    print(" ".join(input_word))
                    break
            if letter_used:
                break

        else:
            print(*input_word)
