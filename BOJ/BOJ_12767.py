from sys import stdin


class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node()
            self.root.data = data
            return

        cur = self.root
        before = cur

        while cur:  # cur이 None이 아닐 때까지
            before = cur  # cur의 부모 노드를 저장
            if cur.data > data:  # cur의 데이터가 data보다 크면
                cur = cur.left  # 왼쪽 자식 노드로 이동
            else:
                cur = cur.right  # 오른쪽 자식 노드로 이동
        cur = Node()
        cur.data = data
        if before.data > data:  # 부모 노드의 데이터가 data보다 크면
            before.left = cur  # 왼쪽 자식 노드로 저장
        else:  # 부모 노드의 데이터가 data보다 작으면
            before.right = cur  # 오른쪽 자식 노드로 저장


n, k = map(int, stdin.readline().split())
tree = [Tree() for _ in range(50)]

for i in range(n):
    inputs = list(map(int, stdin.readline().split()))
    for j in range(k):
        tree[i].insert(inputs[j])


def child(a):
    """
    형태를 비교하기 위해 자식 노드의 유무를 비트로 표현
    0: 자식 노드가 없음
    1: 왼쪽 자식 노드가 있음
    2: 오른쪽 자식 노드가 있음
    3: 왼쪽, 오른쪽 자식 노드가 있음
    """
    t = 0
    if a.left:
        t |= 1 << 1
    if a.right:
        t |= 1 << 2
    return t


def is_same(a, b):
    flag = child(a) == child(b)
    if flag:
        if a.left:
            flag = flag and is_same(a.left, b.left)
        if a.right:
            flag = flag and is_same(a.right, b.right)
    return flag


arr = [-1] * 50
visit = [0] * 50

for i in range(n):
    if arr[i] > -1:
        continue
    arr[i] = i
    for j in range(i + 1, n):
        if arr[j] > -1:  # 이미 같은 번호를 가진 트리가 있으면
            continue
        if is_same(tree[i].root, tree[j].root):  # 같은 모양의 트리인지 확인
            arr[j] = i

answer = 0
for i in range(n):  # 같은 모양의 트리를 찾아서 같은 번호를 부여
    visit[arr[i]] = 1

for i in range(n):  # 같은 번호를 가진 트리의 개수를 세어줌
    answer += visit[i]

print(answer)
