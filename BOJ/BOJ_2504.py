s = input()
stack = []

tmp = 1
res = 0

for i in range(len(s)):
    this = s[i]
    # '(' 일 때, tmp *= 2, stack.append(this)
    if this == '(':
        tmp *= 2
        stack.append(this)
    # '[' 일 때, tmp *= 3, stack.append(this)
    elif this == '[':
        tmp *= 3
        stack.append(this)
    # ')' 일 때, stack가 비어있거나 stack[-1]이 '['이면 res = 0, break
    elif this == ')':
        if not stack or stack[-1] == '[':
            res = 0
            break
        if s[i-1] == '(':
            res += tmp
        tmp //= 2
        stack.pop()
    # ']' 일 때, stack가 비어있거나 stack[-1]이 '('이면 res = 0, break
    else:
        if not stack or stack[-1] == '(':
            res = 0
            break
        if s[i-1] == '[':
            res += tmp
        tmp //= 3
        stack.pop()

# stack에 문자가 남아있으면 res = 0
if stack:
    res = 0
print(res)
