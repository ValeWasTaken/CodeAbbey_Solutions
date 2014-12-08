def fibonacci_search(amount):
        x = 0
        answer = []
        while x < amount:
                fibNum = input()
                a,b,c,count = 0,1,0,0
                while(c <= fibNum and fibNum != 0):
                        c = a + b
                        a = b
                        b = c
                        count += 1
                answer.append(str(count))
                x += 1
        print(' '.join(answer))
fibonacci_search(input())
