N = int(input())
count = 0
for _ in range(N):
    if int(input()) == 1:
        count += 1
    else:
        count -= 1
print("Junhee is ",end="")
if count > 0:
    print("cute!")
else:
    print("not cute!")