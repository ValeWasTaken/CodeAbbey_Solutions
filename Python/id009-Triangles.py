def triangle(calculations):
    answer = []
    for calculation in range(calculations):
        [a,b,c] = raw_input().split()
        [a,b,c] = int(a),int(b),int(c)
        minNum = min(int(a),int(b),int(c))
        maxNum = max(int(a),int(b),int(c))

        for x in [a,b,c]:
            if int(x) != minNum and int(x) != maxNum:
                midNum = x
        a,b,c = minNum, midNum, maxNum
        if (a+b) > c:
            answer.append(str('1'))
        else:
            answer.append(str('0'))
    print(' '.join(answer))
triangle(input())
