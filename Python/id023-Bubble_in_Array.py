# Python 2.7
def check_sum(data):
    result = 0
    
    for number in data:
        result += number
        result *= 113
        result %= 10000007
    return(result)

def bubble_in_array(data):
    numbers = [int(x) for x in data[:-1]]
    swap_count = 0

    for x in xrange(len(numbers)-1):
        if numbers[x] > numbers[x+1]:
            numbers[x+1], numbers[x] = numbers[x], numbers[x+1]
            swap_count += 1
    print('%d %d') % (swap_count, check_sum(numbers))
    
bubble_in_array(raw_input().split())
