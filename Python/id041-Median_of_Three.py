def findMedian(amount):
        answer = []
        for x in range(amount):
                [a, b, c] = raw_input().split()
                minNum = min(int(a), int(b), int(c))
                maxNum = max(int(a), int(b), int(c))
                for x in [a, b, c]:
                    if int(x) != minNum and int(x) != maxNum:
                        answer.append(str(x))
        print(' '.join(answer))
findMedian(input())
