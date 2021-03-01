import sqlite3
from .config import db


def create_table():
    try:
        with sqlite3.connect(db) as conn:  
            conn.execute('CREATE TABLE IF NOT EXISTS artists (artist_name text, email text, unique( artist_name COLLATE NOCASE, email COLLATE NOCASE))')
            conn.execute('CREATE TABLE IF NOT EXISTS track_artwork (artist_name text, artwork text, price int, availability boolean, track_id int, unique(artwork COLLATE NOCASE), foreign key(track_id) references artist(artist_name))')
        
    except Exception as e:
        print('Could not create table ERROR!', e)
    conn.close()

def create_new_artist(artist):
    try:
        with sqlite3.connect(db) as conn:
            conn.execute(f'INSERT INTO artists VALUES(?, ?)', (artist.name, artist.email))
        
        return True
    except sqlite3.IntegrityError as e:
        raise NameError(f'Error - this artist is already in the system') from e
    finally:
        conn.close()

def create_new_artwork(artwork):
    try:
        with sqlite3.connect(db) as conn:
            conn.execute(f'INSERT INTO track_artwork VALUES(?, ?, ?, ?)', (artwork.artist_name, artwork.artwork, artwork.price, artwork.available ))
       
        return True
    except sqlite3.IntegrityError as e:
        raise NameError(f'Error - this artwork is already in the system') from e
    finally:
        conn.close() 

def search_artist(artist):
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM artists WHERE name like ?', (artist.name))
    first_row = results.fetchone()
    if first_row:
        print('The artist is: ', first_row)  
    else:
        print('Not found')
    conn.close()

def search_artwork(artwork):
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM track_artwork WHERE artwork like ?', (artwork.artwork ))
    first_row = results.fetchone()
    if first_row:
        print('The artwork is: ', first_row)  
    else:
        print('Not found')
    conn.close()

def update_availability(artwork):
 
    with sqlite3.connect(db) as conn:
        updated_row = conn.execute('UPDATE track_artwork SET available = ? WHERE artwork = ? ', (artwork.artwork, artwork.availability))
        if updated_row > 0:
            print('Successfully updated!')
        else:
            print('Update did not work, please double check your selection')
    conn.close()
 
 
def delete_artist(artist):
    with sqlite3.connect(db) as conn:
        deleted = conn.execute('DELETE from artists AND track_artwork WHERE artist_name = ?', (artist.name ))
        if deleted > 0 :
            print('Deleted')
        else :
            print('Could not delete.')
    conn.close()
 
 


