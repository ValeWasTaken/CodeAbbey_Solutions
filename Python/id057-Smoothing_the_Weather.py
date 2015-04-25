def smooth(amount, numbers):
    answer = []
    for x in range(amount):
        if x == 0 or x == amount-1:
            answer.append(str(numbers[x]))
        else:
            smoothNum = (float(numbers[x-1]) + float(numbers[x]) + float(numbers[x+1])) / 3
            answer.append(str(smoothNum))
    print(' '.join(answer))
smooth(input(),raw_input().split())
