def wsd(numOfSums): #wsd = Weighted sum of digits
        sums = raw_input().split(' ')
        answer = []
        for number in sums:
                    num = 0
                    digits = list(number)
                    for x in range(len(digits)):
                            num += int(digits[x]) * (x+1)
                    answer.append(str(num))
        print(' '.join(answer))
wsd(input())
# Q: But wait.. Why do you have numOfSums at all? It doesn't do anything.
# A: I know, but it was required for the program. Take it up with CodeAbbey! =p
