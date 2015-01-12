def savingsCalc(calculations):
    answer = []
    for calculation in range(calculations):
        # start = Starting money, end = Goal amount, rate = Interest rate
        start, end, rate = raw_input().split()
        rate = (int(rate) / 100.00) + 1
        start,end = int(start),int(end)
        year = 0
        
        while start < end:
            start *= rate
            year += 1
        answer.append(str(year))
    print(' '.join(answer))
savingsCalc(input())
