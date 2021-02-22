from model import *
from sqlite_db.database import *
from sqlite_db.config import db

def main():
    setup()

    menu_view()

def setup():
    db.create_table()

def create_artist():
    name = input('Artist name:')
    email = input('Email Address:')

    artist = Artist(name, email)
    added = db.create_new_artist(artist)
    if added:
        print('Artist added')

def create_artwork():
    artist_name = input('Artist name: ')
    artwork = input('Artwork: ')
    price = int(input('Price: '))
    availability = input('Availability: ')

    artwork = Artwork(artist_name, artwork, price, availability)
    added = db.create_new_artwork(artwork)
    if added:
        print('Artwork added')
    else:
        print('Artwork already exists')
def search_artist():
    name = input('What artist would you like to find?')
    find_artist = db.search_artist(name)
    if find_artist == None:
        print('Artist not found try again')
    return
def search_artwork():
    artwork_name = input('What artwork are you looking for?')
    find_artwork = db.search_artwork(artwork_name)
    if find_artwork == None:
        print('artwork not found')
    return
def update_available():
    updated_availability = input('Change availability:')
    update_artwork = input('What artwork would you like to update? ')
    updated = db.update_availability(update_artwork,updated_availability)
    if updated == None:
        print('Cant update no such artwork or artist')
    return
def delete_artist_artwork():
    find_artist = input('What artist would you like to delete?')
    deleted = db.delete_artist(find_artist)
    if deleted == 0:
        print('Artist has been deleted')
    else:
        print('No such artist exists')

def menu_view():

    choice = '0'
    while choice == '0':
        print('Main Menu')
        print('1 create new artist ')
        print('2 create new artwork')
        print('3 search artist')
        print('4 search artwork')
        print('5 update artwork avaiabilty')
        print('6 delete selected artist and artwork')
        print('7 quit')
        choice = int(input('What would you like to do?'))

        if choice == "1":
            create_artist()
        elif choice == "2":
            create_artwork
        elif choice == "3":
            search_artist()
        elif choice == "4":
            search_artwork()
        elif choice == "5":
            update_available()
        elif choice == "6":
            delete_artist_artwork()
        elif choice == "7":
            print('Good bye!')
            break
        else:
            print("Please make a proper selection ")

if __name__ == '__main__':
    setup()
    main()

