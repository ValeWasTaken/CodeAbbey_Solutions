# Python 3.4
# Work in progress, currently the program is near the answer but not 100% accurate.

def two_printers():
    tests = int(input())
    answer = []
    for test in range(tests):
        # p1s = Printer #1 Speed, p2s = Printer #2 Speed. (Page per X seconds)
        p1s, p2s, pages = [int(x) for x in input().split()]
        ans = pages / (1/p1s + 1/p2s)
        answer.append(str(ans))
    print(' '.join(answer))
