

sentence = input('What would you like to make camelCase?')
wordList = sentence.split()
capWords = []

for word in wordList:
    capWords.append(word.title())


camelCase = ' '.join(capWords).replace(' ', '')
finWord = camelCase[0].lower() + camelCase[1:]


def show_banner():
    message = "WELCOME to camelCASE TRANSLATOR!"
    print(f'{message}')

def main():
    show_banner()
    print(finWord)

if __name__ == '__main__':
    main()