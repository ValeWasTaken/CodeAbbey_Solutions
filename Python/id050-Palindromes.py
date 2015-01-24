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
        answer = []
        for x in range(wordCount):
                word = cleanWord(raw_input().lower())
                word = ''.join(word)
                if word == word[::-1]:
                        answer.append('Y')
                elif word != word[::-1]:
                        answer.append('N')
        print(' '.join(answer))

isPalindrome(input())
