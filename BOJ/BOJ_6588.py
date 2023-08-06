from sys import stdin

def get_prime_list():
    N = 1000000
    sieve = [True] * N
    m = int(N ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, N, i):
                sieve[j] = False
    return [i for i in range(2, N) if sieve[i] == True], sieve

arr, sieve = get_prime_list()

while True:
    n = int(stdin.readline().rstrip())
    if n == 0:
        break    
    t = False
    for i in range(len(arr)//2):
        if sieve[n - arr[i]]:
            s = "{} = {} + {}".format(n, arr[i], n-arr[i])
            print(s)
            t = True 
            break
        if t:
            break
    