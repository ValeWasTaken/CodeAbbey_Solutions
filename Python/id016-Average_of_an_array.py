def cleanData(data):
        array = []
        for x in data:
                if x != '0' or 0:
                        array.append(x)
        return array

def average(amount):
        answer = []
        for x in range(amount):
                array = raw_input().split()
                array = cleanData(array)
                total, average, y = 0,0,0
                while y < len(array):
                        total += int(array[y])
                        y+=1
                        average = "%.02f" % ((float(total)) / float(len(array)))
                        average = int(round(float(average)))
                answer.append(str(average))
        print(' '.join(answer))
average(input())
