# docstring - name and application 
# imports
import sqlite3

# constants and variables
database = 'fave_manga_draft.db'

# functions
def print_manga_faves():
    # docstring - print all outputs nicely
    fave = input('Rating lower limit: ')
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = 'SELECT * FROM manga_faves WHERE manga_rating >= ? ORDER BY manga_rating DESC;'
    cursor.execute(sql,(fave,))
    results = cursor.fetchall()
    plus = 1
    # loop through the results
    print(f'My current mangas with a rating of {fave} and higher are:')
    for manga in results:
        print(f'Rank {plus :<3}{manga[1]:<30}rating: {manga[5]}')
        plus += 1
    # finish loop here
    db.close

# main codes
if __name__ == '__main__':
    print_manga_faves()


