#Python 3.4

def find_slope(a, b, c, d):
    return (d - b) / (c - a)

def find_intercept(a, b, m):
    return (b - m * a)

def linear_function():
    answer = []
    test_cases = int(input())
    for test_case in range(test_cases):
        a, b, c, d = [int(x) for x in input().split()]
        m = int(find_slope(a, b, c, d))
        g = int(find_intercept(a, b, m))
        answer.append('({0} {1})'.format(m, g))
    print(' '.join(answer))
    
linear_function()
