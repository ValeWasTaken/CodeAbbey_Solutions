def find_Sums(pairAmount):
        pairCount = 0
        answer = []
        while pairCount < pairAmount:
                digits = raw_input()
                numbers = digits.split(' ')
                sum = 0
                for x in range(0, 2):
                        sum += int(numbers[x])
                answer.append(str(sum))
                pairCount += 1
        print(' '.join(answer))
find_Sums(input())
