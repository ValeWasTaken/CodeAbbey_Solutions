# Python 2.7

def gen_primes(limit=3000000):
    ignore_this = raw_input() # CodeAbbey required wasted input.
    data = [int(x) for x in raw_input().split()]
    primes, answer = [], []

    # Sieve of Eratosthenes
    sieve = [True] * (limit + 1)
    for num in range(2, limit + 1):
        if sieve[num]:
           primes.append(num)
           for i in range(num * num, limit + 1, num):
               sieve[i] = False
               
    for number in data:
        answer.append(str(primes[number-1]))
    print(' '.join(answer))
gen_primes()
