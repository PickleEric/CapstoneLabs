
classList = []

def main():

    classNum = input('How many classes are you taking? ')

    for classNum in range(int(classNum)):
        className = input('Name of class: ')
        classList.append(className)
    print('The classes you are taking are: ')
    print(*classList, sep = "\n")

main()