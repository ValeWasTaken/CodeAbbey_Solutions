def find_Sums(pairAmount):
        answer = []
        for pair in range(pairAmount):
                numbers = raw_input().split(' ')
                sum = 0
                for x in range(0, 2):
                        sum += int(numbers[x])
                answer.append(str(sum))
        print(' '.join(answer))
find_Sums(input())
