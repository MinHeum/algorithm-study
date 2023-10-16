from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    # define queue
    q = deque()
    
    # appen begin word and depth
    q.append([begin, 0])
    
    # define visited list
    V = [0] * len(words)
    
    while q:
        w, c = q.popleft()
        if w == target:
            answer = c
            break
        for i in range(len(words)):
            temp = 0
            # check word is not visited
            if not V[i]:
                for j in range(len(w)):
                    if w[j] != words[i][j]:
                        temp += 1
                if temp == 1:
                    q.append([words[i], c+1])
                    V[i] = 1
    return answer