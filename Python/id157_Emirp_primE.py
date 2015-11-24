# Python 3.4
# Note -- The solution is currently a work-in-progress
# It works, but takes a brute-force method that will only
# work on realistic numbers (ie: not a quintillion)

def find_answer(entry):
    for emirp in semirp:
        if emirp > entry:
            return emirp

def gen_primes(limit=300000000):
    data = [int(input()) for x in range(int(input()))]
    primes, semirp, answer = [], [], []
    global semirp

    # Sieve of Eratosthenes
    sieve = [True] * (limit + 1)
    for num in range(2, limit + 1):
        if sieve[num]:
           primes.append(num)
           for i in range(num * num, limit + 1, num):
               sieve[i] = False

    # Find reversable primes
    for prime in primes:
        if int(str(prime)[::-1]) in primes:
            semirp.append(prime)

    # Find answer
    for entry in data:
        answer.append(str(find_answer(entry)))

    print(' '.join(answer))
gen_primes()
