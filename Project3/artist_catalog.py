import sqlite3
 
db = 'artist_artwork_db.sqlite'
""" Your app needs to save this data about each artist:

name
email address
and data about the artworks:

artist
name of artwork - each artist's artwork has a unique name
price
whether the artwork is available, or if it has been sold 
Your application should have these features

add a new artist
search for all the artwork by an artist (everything - available and sold) 
display for all the available artwork by an artist
add a new artwork. Make sure the artwork is associated with an artist. If needed, create an artist first. 
delete an artwork
change the availability status of an artwork, for example, change from available to sold

 """
 
def create_table():
    with sqlite3.connect(db) as conn:  
        conn.execute('CREATE TABLE IF NOT EXISTS artists (artistid int, artist_name text, email text,unique( artist_name COLLATE NOCASE, email COLLATE NOCASE)')
        
        conn.execute('CREATE TABLE IF NOT EXISTS track_artwork (artist_name text, artwork text, price int, available boolean, track_id int, unique( artist COLLATE NOCASE, artwork COLLATE NOCASE,foreign key(trackid) references artist(artistid)')
    conn.close()
 
 
def insert_example_data():
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO artists values (1, "Pablo Picasso", "Ppicasso@gmail.com")')  # add example artist
        conn.execute('INSERT INTO track_artwork values ("Pabloe Picasso", "The Wheeping Woman", 100000, False, 100)') #add example artwork
    conn.close()
 
 
def display_all_artists():
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM artists')
    print('All artists listed: ')
    for row in results:
        print(row)  # each row is a tuple
 
    conn.close()
def display_artwork():
    conn = sqlite3.connect(db)
    search_by_artist = input('Enter Artist Name:')
    result = conn.execute('SELECT * FROM track_artwork WHERE artist_name like ?', (search_by_artist, ))
    if result == None:
        print('There is no artist by that name')
    else:
        print(result)
    return
 
def display_one_artist():
    conn = sqlite3.connect(db)
    artist_info = input('What artist are you looking for?')
    results = conn.execute('SELECT * FROM artists WHERE artist_name like ?', (artist_info, ))
    first_row = results.fetchone()
    if first_row:
        print('Your product is: ', first_row) 
    else:
        print('Not found')
 
 
def create_new_artist():
    new_id = int(input('Enter new id: '))
    new_name = input('Artist name: ')
    new_email = input('Artist eamil:')
 
    with sqlite3.connect(db) as conn:
        conn.execute(f'INSERT INTO artists VALUES(?, ?, ?)', (new_id, new_name, new_email))
 
    conn.close()
#artist_name text, artwork text, price int, available boolean, trackid int
def create_new_artwork():

    new_artwork = input('Artwork name: ')
    new_price = int(input('Price: '))
    new_available = input('Artwork availability:')
    with sqlite3.connect(db) as conn:
        conn.execute(f'INSERT INTO track_artwork VALUES(?, ?, ?)', (new_artwork, new_price, new_available, ))
 
    conn.close()
 
def update_availability():
    updated_availability = input('Change availability:')
    update_artwork = ('What ')
 
    with sqlite3.connect(db) as conn:
        conn.execute('UPDATE track_artwork SET name = ? WHERE id = ? ', (updated_product, update_id))
 
    conn.close()
 
 
def delete_artist(artist_name):
    with sqlite3.connect(db) as conn:
        conn.execute('DELETE from artists and track_artwork WHERE name = ?', (artist_name, ))
    conn.close()
 
 
create_table()
insert_example_data()
