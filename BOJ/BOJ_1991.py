from sys import stdin


# 트리 노드 클래스
class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left if left != "." else None
        self.right = right if right != "." else None


# 전위 순회
def preorder(node):
    print(node.data, end="")
    if node.left:
        preorder(tree[node.left])
    if node.right:
        preorder(tree[node.right])


# 중위 순회
def inorder(node):
    if node.left:
        inorder(tree[node.left])
    print(node.data, end="")
    if node.right:
        inorder(tree[node.right])


# 후위 순회
def postorder(node):
    if node.left:
        postorder(tree[node.left])
    if node.right:
        postorder(tree[node.right])
    print(node.data, end="")


N = int(stdin.readline())

tree = {}

for _ in range(N):
    data, left, right = stdin.readline().split()
    tree[data] = Node(data, left, right)

preorder(tree["A"])
print()
inorder(tree["A"])
print()
postorder(tree["A"])
print()
