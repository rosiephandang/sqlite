print("\nThis is for the bsd fans, ig \n \nWarning, there are spoilers for the series, so if you don't want to know them, click out. \n")

# docstring - name and application 
# imports
import sqlite3

# constants and variables
database = 'BSD_L1_sql_assignment.db'




# 2nd menu functions
def bsd_backstory():
    print('\nBungo Stray Dogs is about...\n')


def bsd_character_menu_1():
    while True:
        first_characters_menu = int(input('\n 1.) All characters \n 2.) Characters with abilities \n 3.) Sort by inspiration \n 4.) Sort by affiliation \n 5.) Sort by age \n 6.) Sort by gender \n 7.) Sort by status \n 8.) Sort by nationality \n 9.) Back to main menu'))

# navigation main menu
def bsd_main_menu():
    while True:
        main_menu = int(input('\nMain menu: \n \n 1.) A bit about Bungo Stray Dogs before you get started. \n 2.) Characters database \n 3.) Exit menu \n \n'))
        if main_menu == 1:
            bsd_backstory()
        

# intro main menu function
intro = input("Enter 'yes' to keep going.\n")
if intro == 'yes':
    bsd_main_menu()

