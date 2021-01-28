from datetime import date

now = date.today()

name = input('What do you go by? ')
birthMonth = input('What month were you born? ')
print(f'HI! {name}!')
print(f'Todays date: {now}')
if birthMonth.lower() == 'november':
    print(f'Happy birthday {name}! ')

print(f'There are {len(name)} letters in your name. ')