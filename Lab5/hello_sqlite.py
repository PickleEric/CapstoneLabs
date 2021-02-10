import sqlite3

db = 'first_db.sqlite'

def create_table():
    with sqlite3.connect(db) as conn:# connect or create new if not exist
        conn.execute('CREATE TABLE IF NOT EXISTS products (id int, name text) ')
    conn.close()

def insert_example_data():
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO products values (1000, "hat")')
        conn.execute('INSERT INTO products values (1001, "jacket")')
    conn.close()

    results = conn.execute('SELECT * FROM products')
    
    for row in results:
        print(row[1]) # Each row is a tuple.

    results = conn.execute('SELECT * FROM products WHERE name like "jacket"') 
    first_row = results.fetchone()
    print(first_row)

    #new_id = int(input('enter new id: '))
    #new_name = input('enter new product: ')

    #conn.execute(f'INSERT INTO products VALUES (?, ?)', (new_id, new_name) )


    update_product = 'wool hat'
    update_id = 1000
    conn.execute('UPDATE products SET name = ? WHERE id = ?', (update_product, update_id))

    delete_product = 'jacket'
    conn.execute('DELETE from PRODUCTS WHERE name = ?', (delete_product, ))

conn.close() # always need close connection

create_table()
insert_example_data()
display_all_data()
create_new_product()
delete_product()