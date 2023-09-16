import functools


def solution(numbers):
    numbers = list(map(str, numbers))
    def compare(x, y):
        return int(y + x) - int(x + y)
    
    numbers.sort(key=functools.cmp_to_key(compare))
    return str(int(''.join(numbers)))