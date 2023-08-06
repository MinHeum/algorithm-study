s = input()
a = s[0:int(len(s)/2)]
b = s[int(len(s)/2):]
asum = 0
bsum = 0
for i in a:
    asum += int(i)
for i in b:
    bsum += int(i)
if asum == bsum:
    print("LUCKY")
else:
    print("READY")