def arrayCount(dataRange, numbers):
    maxVariable = int(dataRange[1])
    answer = []
    
    for num in range(1,maxVariable+1):
        answer.append(str(numbers.count(num)))
    print(' '.join(answer))
arrayCount(raw_input().split(),[int(x) for x in raw_input().split()])
