def sumDigits(sumCount):
        answer = []
        for eachLine in range(sumCount):
                [a,b,c] = raw_input().split(' ')
                value = (int(a) * int(b)) + int(c)
                value = list(str(value))
                sum = 0
                for digit in value:
                        sum += int(digit)
                answer.append(str(sum))
        print(' '.join(answer))
sumDigits(input())
