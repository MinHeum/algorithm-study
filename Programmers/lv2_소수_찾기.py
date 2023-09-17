from itertools import permutations

def solution(numbers):
    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
    answer = 0

    numbers = list(numbers)

    # 만들 수 있는 모든 수
    all_numbers = set()

    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers, i):
            all_numbers.add(int(''.join(j)))

    for n in all_numbers:
        if is_prime(n):
            answer += 1

    return answer
