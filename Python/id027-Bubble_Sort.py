def bubbleSort(amount, numbers):
    sorted = False
    swapCount, passCount = 0,0

    while not sorted:
        sorted = True
        for i in range(amount-1):
            if numbers[i] > numbers[i+1]:
                sorted = False
                swapCount += 1
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
        passCount += 1
    print('%s %s') % (passCount, swapCount)

bubbleSort(input(),[int(x) for x in raw_input().split()])
