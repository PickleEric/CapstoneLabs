class Author:
    def __init__(self, name): # where the author name and books are stored. 
        self.name = name
        self.books = []

    def publish(self, title):
        self.books.append(title) if title not in self.books else None # appends book name to list and will not allow dublicates 

    def __str__(self):
        titles = ', '.join(self.books) or 'No published books' # the format of the returned string
        return f'{self.name}. Books: {titles}'

def main(): # our main funciton

    kurt = Author('Kurt V')
    kurt.publish('Slaughter House Five')
    kurt.publish('Cats Craddle')
    kurt.publish('Cats Craddle')
    print(kurt)

    eric = Author('Eric R')
    print(eric)

main() # dont forget to call the main function