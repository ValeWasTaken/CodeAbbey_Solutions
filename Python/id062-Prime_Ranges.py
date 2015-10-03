# Python 3.4
def gen_primes(a, limit):
    primes = []

    # Sieve of Eratosthenes
    sieve = [True] * (limit + 1)
    for num in range(2, limit + 1):
        if num < a:
            pass
        if sieve[num]:
           if num >= a:
               primes.append(num)
           for i in range(num * num, limit + 1, num):
               sieve[i] = False
    return primes

def primes_between():
  searches = int(input())
  answer = []
  for search in range(searches):
    a, b = input().split()
    a, b = int(a), int(b)
    primes = gen_primes(a, b)
    count = len(str(primes).split())
    answer.append(str(count))
  print(' '.join(answer))
primes_between()
