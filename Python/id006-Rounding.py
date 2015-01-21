def roundNums(amount):
    answers = []
    for pairCount in range(amount):
        pair = raw_input().split(' ')
        answers.append(str(int(round(float("%.02f" % (float(pair[0]) / float(pair[1])))))))
    print(' '.join(answers))
roundNums(input())
