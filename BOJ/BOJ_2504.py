s = input()
stack = []

tmp = 1
res = 0

for i in range(len(s)):
    this = s[i]   
    if this == '(':
        tmp *= 2
        stack.append(this)
    elif this == '[':
        tmp *= 3
        stack.append(this)

    elif this == ')':
        if not stack or stack[-1] == '[':
            res = 0
            break
        if s[i-1] == '(':
            res += tmp
        tmp //= 2
        stack.pop()  
    else:
        if not stack or stack[-1] == '(':
            res = 0
            break
        if s[i-1] == '[':
            res += tmp
        tmp //= 3
        stack.pop() 

if stack:
    res = 0
print(res)