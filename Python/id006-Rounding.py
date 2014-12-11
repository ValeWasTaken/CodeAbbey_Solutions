def roundNums(amount):
    pairCount = 0
    answers = []
    while pairCount < amount:
        pair = raw_input()
        numbers = pair.split(' ')
        answer = "%.02f" % (float(numbers[0]) / float(numbers[1]))
        answer = int(round(float(answer)))
        answers.append(str(answer))
        pairCount += 1
    print(' '.join(answers))
roundNums(input())
