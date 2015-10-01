# Python 3.4
from collections import Counter

def check_anagram():
    amount = int(input()) # Amount of words to check (CodeAbbey requirement.)
    answer = []
    
    for check in range(amount):
        word = input()
        word_data = Counter(word) # Count the letter composition
        count = 0 # Amount of anagrams found for the word.
        
        with open('words.txt', 'r') as f:
            for line in f.readlines():
                line = line.replace('\n', '') # Remove spaces from the file.
                anagram_data = Counter(line) # Count letter composition of word.
                if word_data == anagram_data and word != line:
                    count += 1 # If letter compisiton matches and ..
                               # the word is not the exact word, count it.
        answer.append(str(count)) # Store answer and reset for next word.
        anagram_count = 0
    print(' '.join(answer))
check_anagram()
