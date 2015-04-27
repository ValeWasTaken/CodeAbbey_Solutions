def sortIndexes(amount, values):
    answer = []
    sortedValues = sorted(values)
    for sortedValue in sortedValues:
        for x in range(amount):
            if sortedValue == values[x]:
                answer.append(str(x+1))
    print(' '.join(answer))
sortIndexes(input(),[int(x) for x in raw_input().split()])
