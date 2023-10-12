from sys import stdin

# 절댓값 힙 구현

class AbsHeap:
  def __init__(self):
    self.heap = [None]
    self.size = 0

  # push 함수
  # 배열의 맨 끝에 x를 추가하고, sift up 수행
  def push(self, x):
    self.heap.append(x)
    self.size += 1
    self._sift_up(self.size)

  # pop 함수
  def pop(self):
    # 배열이 비어있으면 0을 return
    if self.size == 0:
      return 0
    # 배열의 맨 끝에 있는 원소와 swap한 뒤,
    # 맨 끝에 있는 원소를 pop하고, sift down 수행
    else:
      self._swap(1, self.size)
      result = self.heap.pop()
      self.size -= 1
      self._sift_down(1)
      return result

  # 부모 노드와 swap
  def _sift_up(self, i):
    while i > 1:
      parent = i // 2
      if self._compare(i, parent):
        self._swap(i, parent)
        i = parent
      else:
        break

  # 자식 노드 중 절댓값이 더 작은 노드와 swap
  def _sift_down(self, i):
    while i * 2 <= self.size:
      left = i * 2
      right = i * 2 + 1
      if right <= self.size:
        if self._compare(right, left):
          child = right
        else:
          child = left
      else:
        child = left
      if self._compare(child, i):
        self._swap(i, child)
        i = child
      else:
        break

  # swap 함수
  def _swap(self, i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

  # 절댓값 비교 함수 (절댓값이 서로 같다면 원래 수 비교)
  def _compare(self, i, j):
    if abs(self.heap[i]) < abs(self.heap[j]):
      return True
    elif abs(self.heap[i]) == abs(self.heap[j]):
      if self.heap[i] < self.heap[j]:
        return True
      else:
        return False
    else:
      return False
    
heap = AbsHeap()

N = int(stdin.readline().rstrip())

for _ in range(N):
  x = int(stdin.readline().rstrip())
  # 0이면 pop, 아니면 push
  if x == 0:
    print(heap.pop())
  else:
    heap.push(x)
