print("\nThis is for the bsd fans, ig \n \nWarning, there are spoilers for the series, so if you don't want to know them, click out. \n")

# docstring - name and application 
# imports
import sqlite3
import sys

# constants and variables
database = 'BSD_L1_sql_assignment.db'

# exit function
def exit_option():
    print('\nHopefully that was helpful or entertaining :)')
    sys.exit()



# actual query functions
def all_characters():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = 'SELECT name, job, titles FROM bsd_characters ORDER BY name ASC;'
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'All characters:\n')
    for character in results:
        print(f'Name: {character[0]:<36}Job: {character[1]:<75}Titles: {character[2]}\n')
    # finish loop here
    db.close

# 2nd menu functions
def bsd_backstory():
        print('\nBungo Stray Dogs is about...\n')
        while True:
            exit = input("Do you want to back to main menu? 'yes' or 'no' answers only please.\n")
            if exit == 'yes':
                bsd_main_menu()
            if exit == 'no':
                exit_option()
                break
           
def bsd_character_menu_1():
    while True:
        first_characters_menu = int(input('\nCharacters menu:\n 1.) All characters \n 2.) Characters with abilities \n 3.) Sort by inspiration \n 4.) Sort by affiliation \n 5.) Sort by age \n 6.) Sort by gender \n 7.) Sort by status \n 8.) Sort by nationality \n 9.) Back to main menu\n\n'))
        if first_characters_menu == 1:
            all_characters()
        if first_characters_menu == 9:
            bsd_main_menu()

# navigation main menu
def bsd_main_menu():
    while True:
        try:
            main_menu = int(input('\nMain menu: \n 1.) A bit about Bungo Stray Dogs before you get started. \n 2.) Characters database \n 3.) Exit menu \n \n'))
            if main_menu == 1:
                bsd_backstory()
                break
            if main_menu == 2:
                bsd_character_menu_1()
            if main_menu == 3:
                exit_option()
                break
            if main_menu != 1 or main_menu != 2 or main_menu != 3: 
                print('\nEnter a number between 1-3, please.\n')
        except ValueError:
            print('\nEnter a number between 1-3, please.\n')
        

# intro main menu function
while True:
    intro = input("Enter 'yes' to keep going, or 'no' to stop:\n")
    if intro == 'yes':
        bsd_main_menu()
    if intro == 'no':
        exit_option()
        break


