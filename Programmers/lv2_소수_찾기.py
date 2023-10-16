from itertools import permutations

def solution(numbers):
    def eratos(n):
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i + i, n + 1, i):
                    sieve[j] = False

        return sieve
    

    numbers = list(numbers)

    # 만들 수 있는 모든 수
    all_numbers = set()

    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers, i):
            all_numbers.add(int(''.join(j)))

    # 소수 판별
    sieve = eratos(max(all_numbers))
    answer = 0

    for num in all_numbers:
        if sieve[num]:
            answer += 1

    return answer
