from sys import stdin


N = int(stdin.readline())

image = [list(stdin.readline().rstrip()) for _ in range(N)]

answer = ""


def all_is_same(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if image[i][j] != image[x][y]:
                return False
    return True


def solve(x, y, size):
    global answer

    if all_is_same(x, y, size):
        answer += image[x][y]
        return

    new_size = size // 2

    answer += "("
    solve(x, y, new_size)
    solve(x, y + new_size, new_size)
    solve(x + new_size, y, new_size)
    solve(x + new_size, y + new_size, new_size)
    answer += ")"
    return


solve(0, 0, N)
print(answer)
