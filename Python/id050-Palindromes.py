def cleanWord(data):
        word = []
        for char in data:
                if str.isalpha(char) == True:
                        word.append(char)
                elif str.isalpha(char) == False:
                        char = ''
                        word.append(char)
        return word

def isPalindrome(wordCount):
        x = 0
        answer = []
        while x < wordCount:
                data = raw_input().lower()
                word = cleanWord(data)

                word = ''.join(word)
                if word == word[::-1]:
                        answer.append('Y')
                elif word != word[::-1]:
                        answer.append('N')
                x+=1
        print(' '.join(answer))

isPalindrome(input())
