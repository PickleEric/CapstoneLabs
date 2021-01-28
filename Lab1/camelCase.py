

sentence = input('What would you like to make camelCase?')
wordList = sentence.split()
capWords = []

for word in wordList:
    capWords.append(word.title())


camelCase = ' '.join(capWords).replace(' ', '')
finWord = camelCase[0].lower() + camelCase[1:]
print(finWord)


