def checkSum(numbers):
    array = raw_input().split()
    result = 0
    
    for number in range(numbers):
        result += int(array[number])
        result *= 113
        result %= 10000007
        
    print(result)
checkSum(input())
