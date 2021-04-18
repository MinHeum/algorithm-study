T = int(input())
for _ in range(T):
    arr1 = [0] * 26
    arr2 = [0] * 26
    word_a, word_b = map(str, input().split())
    for i in word_a:
        arr1[ord(i)-97] += 1
    
    for i in word_b:
        arr2[ord(i)-97] += 1
    
    is_anagrams = True

    for i in range(0,26):
        if arr1[i] != arr2[i]:
            is_anagrams = False
            break
    
    print("{0} & {1} are ".format(word_a, word_b), end="")
    if is_anagrams:
        print("anagrams.")
    else:
        print("NOT anagrams.")
