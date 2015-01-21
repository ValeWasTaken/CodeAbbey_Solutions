def findMin(amount):
        answer = []
        for pairCount in range(amount):
                pair = raw_input().split(' ')
                answer.append(str(min(int(pair[0]),int(pair[1]))))
        print(' '.join(answer))
findMin(input())
