def findMin(amount):
        answer = []
        for x in range(amount):
                [a, b, c] = raw_input().split()
                minNum = min(int(a), int(b), int(c))
                answer.append(str(minNum))
        print(' '.join(answer))
findMin(input())
