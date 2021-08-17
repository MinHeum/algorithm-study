import heapq

count = int(input())

min_heap = list(map(int, input().split()))
max_heap = min_heap[:]
max_heap = list(map(lambda x : x * -1, min_heap[:]))

heapq.heapify(min_heap)
heapq.heapify(max_heap)

while count > 0:
    min = heapq.heappop(min_heap) + 1
    heapq.heappush(min_heap, min)
    max = heapq.heappop(max_heap) + 1
    heapq.heappush(max_heap, max)
    count -= 1

answer = heapq.heappop(max_heap) * -1 - heapq.heappop(min_heap)

print("ANSWER:"+str(answer))