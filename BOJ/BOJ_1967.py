from sys import stdin

n = int(stdin.readline().rstrip())  # 노드의 개수

tree = [[] for _ in range(n + 1)]  # 트리

for _ in range(n - 1):
    parent, child, weight = map(int, stdin.readline().split())
    # 부모 노드의 자식 노드로 가는 간선의 가중치
    tree[parent].append((child, weight))
    # 자식 노드의 부모 노드로 가는 간선의 가중치
    tree[child].append((parent, weight))

# dfs 함수 정의


def dfs(start):
    visited = [False] * (n + 1)  # 방문 여부
    stack = [(start, 0)]  # dfs를 위한 스택
    visited[start] = True  # 시작 노드 방문 처리
    max_node, max_weight = 0, 0  # 최대 가중치를 가지는 노드와 그 가중치

    while stack:
        node, weight = stack.pop()  # 현재 노드와 가중치

        if weight > max_weight:  # 현재 가중치가 최대 가중치보다 크면
            max_node, max_weight = node, weight  # 최대 가중치를 가지는 노드와 그 가중치 갱신

        for next_node, next_weight in tree[node]:
            # 다음 노드와 다음 노드로 가는 간선의 가중치
            if not visited[next_node]:  # 다음 노드를 방문하지 않았으면
                visited[next_node] = True  # 다음 노드 방문 처리
                stack.append((next_node, weight + next_weight))  # 스택에 추가

    return max_node, max_weight  # 최대 가중치를 가지는 노드와 그 가중치 반환


print(dfs(dfs(1)[0])[1])  # 루트 노드에서 가장 먼 노드를 찾고, 그 노드에서 가장 먼 노드까지의 거리를 출력
