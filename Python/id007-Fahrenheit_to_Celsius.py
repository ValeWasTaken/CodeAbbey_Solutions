def convert(variables):
    variables = variables.split()
    del variables[0]    
    x = 0
    answer = []
    while x < len(variables):
        num = float(variables[x])
        num = round(float((num) - 32) * (5.0/9.0))
        answer.append(str(int(num)))
        x += 1
    print(' '.join(answer))
convert(raw_input())
