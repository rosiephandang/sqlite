import sqlite3

print('Hello, testing, testing...')

def print_manga_faves():
    fave = input('Rating lower limit: ')
    db = sqlite3.connect('fave_manga_draft.db')
    cursor = db.cursor()
    sql = 'SELECT * FROM manga_faves WHERE manga_rating >= ? ORDER BY manga_rating DESC;'
    cursor.execute(sql,(fave,))
    results = cursor.fetchall()
    plus = 1
    for manga in results:
        print(f'Out of my highest rated mangas currently, at rank {plus}, is {manga[1]}, with a rating of {manga[5]}.')
        plus += 1
    db.close

if __name__ == '__main__':
    print_manga_faves()

print('hmmm, still testing , testing')

