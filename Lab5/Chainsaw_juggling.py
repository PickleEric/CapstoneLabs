import sqlite3

# validation errors, rowid

db = 'juggling_records.sqlite'
#def menu_options():
    #print('World Juggling Records!')
    #print('1 View all')
    #print('2 Add')
    #print('3 Display one record')
    #print('4 Delete record')
    #loop=True      
  
    #while loop:          ## While loop which will keep going until loop = False
        #menu_options()    ## Displays menu
    #choice = input("Enter your choice [1-5]: ")
     
    #if choice==1:     
        #print ("Menu 1 has been selected")
        #display_all_data()
    #elif choice==2:
        #print ("Menu 2 has been selected")
        #create_new_record()
    #elif choice==3:
        #print ("Menu 3 has been selected")
        #display_one_record(records_name = input('Whos record would you like to see?'))
    #elif choice==4:
        #print ("Menu 4 has been selected")
        #delete_record(records_name= input("Who would you like to delete? "))
    #elif choice==5:
        #print('Menu 5 has been selected')
        #display_one_record(records_name = input('What record would you like to view?'))
        #loop=False 
    
def create_table():
    with sqlite3.connect(db) as conn:  # connect or create new if not exist
        conn.execute('CREATE TABLE IF NOT EXISTS records (name text, country text, catches int)')
    conn.close()
 
 
def insert_example_data():
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO records values ("Janne Mustonen", "Finland", 98)')  # add example record
        conn.execute('INSERT INTO records values ("Ian Stewart", "Canada", 94)')  # add example record
        conn.execute('INSERT INTO records values ("Aaron Gregg", "Canada", 88)')  # add example record
        conn.execute('INSERT INTO records values ("Chad Taylor", "USA", 78)')  # add example record
    conn.close()
 
 
def display_all_data():
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM records')
    print('All Juggling records: ')
    for row in results:
        print(row)  # each row is a tuple
 
    conn.close()
 
 
def display_one_record(records_name):
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM records WHERE name like ?', (records_name, ))
    first_row = results.fetchone()
    if first_row:
        print('The record is: ', first_row)  
    else:
        print('Not found')
 
 
def create_new_record():
    new_name = input('Enter Jugglers name: ')
    new_country = input('Enter Home Country: ')
    new_record = int(input('Enter number of Juggles:'))
 
    with sqlite3.connect(db) as conn:
        conn.execute(f'INSERT INTO records VALUES(?, ?, ?)', (new_name, new_country, new_record))
 
    conn.close()
 
def delete_record(records_name):
    with sqlite3.connect(db) as conn:
        conn.execute('DELETE from RECORDS WHERE name = ? COLLATE NOCASE', (records_name, ))
    conn.close()
 
 
create_table()
insert_example_data()
display_one_record(records_name = input('What record would you like to view?'))
display_all_data()
create_new_record()
delete_record(records_name= input("Who would you like to delete? "))


print('end of program!')
