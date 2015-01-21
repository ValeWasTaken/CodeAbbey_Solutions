def findMin(amount):
        pairCount = 0
        answer = []
        for pairCount in range(amount):
                pair = raw_input().split(' ')
                num1,num2 = int(pair[0]),int(pair[1])
                if num1 < num2:
                        answer.append(str(num1))
                else:
                        answer.append(str(num2))
        print(' '.join(answer))
findMin(input())
