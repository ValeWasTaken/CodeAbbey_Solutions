def findMin(amount):
        pairCount = 0
        answer = []
        while pairCount < amount:
                pair = raw_input()
                numbers = pair.split(' ')
                num1 = int(numbers[0])
                num2 = int(numbers[1])
                if num1 < num2:
                        num3 = num1
                else:
                        num3 = num2
                answer.append(str(num3))
                pairCount += 1
        print(' '.join(answer))
findMin(input())
