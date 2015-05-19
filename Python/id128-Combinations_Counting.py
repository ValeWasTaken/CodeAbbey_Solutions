# Python 2.7
def factorial_of(number):
    ans = 1
    for x in range(1,number+1):
        ans *= x
    return ans

def combinations_counting(test_cases):
    answer = []
    for x in range(test_cases):
        n, k = [int(x) for x in raw_input().split()]
        case_answer = factorial_of(n) / (factorial_of(k) * factorial_of(n - k))
        answer.append(str(case_answer))
    print(' '.join(answer))
        
combinations_counting(input())
