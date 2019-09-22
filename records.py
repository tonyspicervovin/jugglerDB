import sqlite3
db_url = "records.db"

class RecordError(Exception):
    pass
def addJuggler():
    name = input("Enter the name of the juggler \n")
    country = input("Enter their Country \n ")
    catches = float(input("Enter the number of catches \n "))
    add_record_holder(name, country, catches)
    ##function to add juggler, calls record holder with name country and catches

def searchName():
    search_name = input("Enter the name to search for \n")
    with sqlite3.connect(db_url) as conn:
        buddy = conn.execute('SELECT * from JUGGLERS WHERE name LIKE ?', (search_name,))
        for row in buddy:
            print("Name: "+row[0]+"\nCountry: "+row[1]+"\nCatches: "+str(row[2]))
    if buddy.rowcount == 0:
        print("Name not found")
    conn.close()
##searching for jugglers

def deleteName():
    delete_name = input("Enter a name to delete")
    with sqlite3.connect(db_url) as conn:
        deleted = conn.execute('DELETE FROM JUGGLERS WHERE name like ?', (delete_name,))
        deleted_count = deleted.rowcount
    conn.close()

    if deleted_count == 0:
        print("Name not found")
    else:
        print(delete_name + " deleted")
    ##deleting juggler
def add_record_holder(name, country, catches):
    print(name+country)
    if not name:
        raise RecordError('Provide a record holder name')
    if not country:
        raise RecordError('Provide a Country')
    if not isinstance(catches, (int, float)) or catches < 0:
        raise RecordError('Provide a positive number for catches')

    with sqlite3.connect(db_url) as conn:
        conn.execute('CREATE table if not EXISTS JUGGLERS (name text, country text, catches integer)')
        rows_mod = conn.execute('UPDATE JUGGLERS set catches = ? WHERE name = ?', (catches, name))
        if rows_mod.rowcount == 0:
            conn.execute('INSERT INTO JUGGLERS VALUES (?, ?, ?)', (name, country, catches))
    conn.close()
    ##adding a new juggler
def main():

    while True:
        choice =int(input("MENU \n1: Add juggler \n2: Search by name \n3: Delete by name \n4: Exit  \n"))
        if choice == 1:
            addJuggler()
        elif choice == 2:
            searchName()
        elif choice == 3:
            deleteName()
        elif choice == 4:
            break
        else:
            print("Unknown option selected")
#menu
if __name__ == '__main__':
    main()
