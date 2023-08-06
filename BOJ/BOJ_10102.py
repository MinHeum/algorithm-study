from sys import stdin

V = int(stdin.readline().rstrip())
vote = stdin.readline().rstrip()

a = vote.count('A')
b = vote.count('B')

if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('Tie')
