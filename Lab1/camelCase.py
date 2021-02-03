capWords = []
def camel_case(sentence):
    
    wordList = sentence.split()
    for word in wordList:
        capWords.append(word.title())

    camelCase = ' '.join(capWords).replace(' ', '')
    finSentence = camelCase[0].lower() + camelCase[1:]

    return finSentence

def main():
    
    sentence = input('What would you like to make camelCase?')
    camelCase = camel_case(sentence)
    print(camelCase)

if __name__ == '__main__':
    main()


