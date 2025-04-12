# docstring - name and application 
# imports
import sqlite3

# constants and variables
database = 'fave_manga_draft.db'

# functions
def print_manga():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = 'SELECT * FROM manga_faves ORDER BY manga_rating DESC;'
    cursor.execute(sql)
    results = cursor.fetchall()
    plus = 1
    # loop through the results
    print(f'My current favourite manga ranked are:')
    for manga in results:
        print(f'Rank {plus :<5}{manga[1]:<30}Rating: {manga[5]:<10}Author: {manga[2]:<20}Artist: {manga[3]}')
        plus += 1
    # finish loop here
    db.close

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
    print(f'My current manga with a rating of {fave} and/or higher are:')
    for manga in results:
        print(f'Rank {plus :<5}{manga[1]:<30}Rating: {manga[5]}')
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
    print(f'My current manga with a rating of {fave} and/or lower are:')
    for manga in results:
        lower += 1
        minus = len(manga) - lower
        print(f'Rank {minus :<5}{manga[1]:<30}Rating: {manga[5]}')
        
    # finish loop here
    db.close

def print_manga_author_is_also_artist():
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = 'SELECT * FROM manga_faves WHERE manga_author = manga_artist;'
    cursor.execute(sql)
    results = cursor.fetchall()
    # looping through results
    for i in results:
        print(f'A manga with the same author and artist is {i[1]}, by {i[2]}')


# main codes
while True:
    ask_menu = input('\nWhat to you want to know? \n 1.) All my current favourites. \n 2.) The highest rated manga out of my current favourites. \n 3.) The lowest rated manga out of my current favourites. \n 4.) Manga with the same author and artist \n 5.) Exit menu \n ')
    if ask_menu == '1':
        print_manga()
    elif ask_menu == '2':
        print_manga_rating_lower_limit()
    elif ask_menu == '3':
        print_manga_rating_upper_limit()
    elif ask_menu == '4':
        print_manga_author_is_also_artist()
    elif ask_menu == '5':
        break
    else:
        print('That was not a choice :) \nChoose one of the options. ')
    
# a lil sumthin to remember
if __name__ == '__main__':
    print('testing, testing')


