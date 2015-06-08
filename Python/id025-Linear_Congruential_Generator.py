# Python 2.7

def find_nth(entries):
    answer = []
    for x in range(entries):
        A, C, M, X0, N = [int(x) for x in raw_input().split()]
        x_cur = X0
        for x in range(N):
            x_next = (A * x_cur + C) % M
            x_cur = x_next
        answer.append(str(x_cur))
    print(' '.join(answer))
find_nth(input())
