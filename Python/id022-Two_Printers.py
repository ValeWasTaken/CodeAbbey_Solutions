# Python 3.4

def two_printers():
    tests = int(input())
    answer = []
    for test in range(tests):
        x, y, n = [float(x) for x in input().split()]
        a = int(y * n / (x + y))
        b = int(x * n / (x + y))

        answer_1 = int(max((a + 1) * x, b * y))
        answer_2 = int(max(a * x, (b + 1) * y))

        answer.append(str(min(answer_1, answer_2)))
    print(' '.join(answer))
two_printers()
