def vowelCount(words):
        vowels = list("aeiouy")
        answer = []
        for x in range(words):
                phraseCount = raw_input().lower()
                phraseCount = sum(phraseCount.count(c) for c in vowels)
                answer.append(str(phraseCount))
        print(' '.join(answer))
vowelCount(input())
