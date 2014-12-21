def BMI(users):
        pairCount = 0
        answer = []
        while pairCount < users:
                pair = raw_input()
                numbers = pair.split(' ')
                weight = float(numbers[0])
                height = float(numbers[1])
                BMI = float(weight / (height * height))

                if BMI < 18.5:
                        answer.append(str('under'))
                elif BMI >= 18.5 and BMI < 25.0:
                        answer.append(str('normal'))
                elif BMI >= 25.0 and BMI < 30.0:
                        answer.append(str('over'))
                elif BMI >= 30.0:
                        answer.append(str('obese'))
                else:
                        print("Error.")
                pairCount += 1
        print(' '.join(answer))
BMI(input())
