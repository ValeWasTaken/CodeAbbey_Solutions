def modCalc(num):
        calc = raw_input()
        while calc[:1] != "%":
                if calc[:1] == '+':
                        num += int(calc[2:].strip())
                elif calc[:1] == '*':
                        num *= int(calc[2:].strip())
                calc = raw_input()
        num %= int(calc[2:].strip()) 
        print(num)
modCalc(input())
