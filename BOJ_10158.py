w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x = (p + t) % (w*2)
y = (q + t) % (h*2)

if x > w:
	x = (2 * w) - x
if y > h:
	y = (2 * h) - y

print("{} {}".format(x, y))