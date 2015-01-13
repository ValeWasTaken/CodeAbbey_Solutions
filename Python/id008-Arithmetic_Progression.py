def progressionCalc(calculations):
    answer = []
    for calculation in range(calculations):
        a,b,c = raw_input().split()
        a,b,c = int(a), int(b), int(c)
        total = 0
        
        for x in range(c):
            total += (a + (b*x))
        answer.append(str(total))
    print(' '.join(answer))
progressionCalc(input())
