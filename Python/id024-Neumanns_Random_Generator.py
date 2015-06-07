# Python 3.4.3

def neumanns(inputs):
    answer = []
    for num in [int(x) for x in input().split()]:
        loop_count = 0
        new_num = num * num
        temp = ''
        repeats = [str(num)]
        no_repition = True

        while no_repition:
            if loop_count != 0:
                new_num = int(new_num) * int(new_num)
                
            new_num = str(new_num)
            while len(new_num) < 8:
                new_num = '0' + new_num
            new_num = new_num[2:-2]

            loop_count += 1
            if new_num in repeats:
                no_repition = False
                
            repeats.append(new_num)
        answer.append(str(loop_count))
    print(' '.join(answer))
neumanns(input()) # This is input() is required to be wasted. Please ignore.
