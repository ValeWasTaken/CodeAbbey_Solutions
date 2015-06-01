# Python 3.4

def check_brackets(checks):
    answer = []
    for check in range(checks):
        raw_data = input()
        data = (''.join([char for char in raw_data if char in('(){}[]<>')]))
        
        # Set higher than len(data) to make sure while loop initates.
        old_data_length = len(data) + 1
        
        while len(data) < old_data_length:
            old_data_length = len(data)
            data = data.replace('()','').replace('{}','').replace('[]','').replace('<>','')

        if len(data) > 0:
            answer.append('0') # String had incorrect bracket usage.
        else:
            answer.append('1') # String had completely correct bracket usage.
    print(' '.join(answer))
check_brackets(int(input()))
