# docstring - name and application 
# imports
import sqlite3

# constants and variables
database = 'fave_manga_draft.db'

# functions
def print_manga_rating_lower_limit():
    # docstring - print all outputs nicely
    fave = input('Rating lower limit: ')
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = 'SELECT * FROM manga_faves WHERE manga_rating >= ? ORDER BY manga_rating DESC;'
    cursor.execute(sql,(fave,))
    results = cursor.fetchall()
    plus = 1
    # loop through the results
    print(f'My current mangas with a rating of {fave} and/or higher are:')
    for manga in results:
        print(f'Rank {plus :<3}{manga[1]:<30}rating: {manga[5]}')
        plus += 1
    # finish loop here
    db.close

def print_manga_rating_upper_limit():
    # docstring - print all outputs nicely
    fave = input('Rating upper limit: ')
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = 'SELECT * FROM manga_faves WHERE manga_rating <= ? ORDER BY manga_rating ASC;'
    cursor.execute(sql,(fave,))
    results = cursor.fetchall()
    lower = 0
    # loop through the results
    print(f'My current mangas with a rating of {fave} and/or lower are:')
    for manga in results:
        lower += 1
        minus = len(manga) - lower
        print(f'Rank {minus :<3}{manga[1]:<30}rating: {manga[5]}')
        
    # finish loop here
    db.close

def print_manga_author_is_also_artist():
    sql = 'SELECT * FROM manga_faves WHERE manga_author = manga_artist;'


# main codes
if __name__ == '__main__':
    print_manga_rating_upper_limit()


