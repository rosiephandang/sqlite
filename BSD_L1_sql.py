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
    print(f'\nAll characters:\n')
    for character in results:
        print(f'Name: {character[0]:<36}Job: {character[1]:<75}Titles: {character[2]}\n')
    # finish loop here
    db.close

def characters_with_abilities():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT name, ability, job FROM bsd_characters WHERE NOT ability = 'n' ORDER BY name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nAll characters with abilities:\n')
    for character in results:
        print(f'Name: {character[0]:<36}Ability: {character[1]:<35}Job: {character[2]}\n')
    # finish loop here
    db.close

def ada_character_affiliation():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT bsd_characters.name, bsd_characters.job, affiliation.affiliation_name FROM bsd_characters JOIN character_affiliation ON bsd_characters.id = character_affiliation.character_id JOIN affiliation ON affiliation.affiliation_id = character_affiliation.affiliation_id WHERE affiliation.affiliation_name = 'Armed Detective Agency' ORDER BY bsd_characters.name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'Characters affiliated with the Armed Detective Agency are:\n')
    for i in results:
        print(f'Name: {i[0]:<30}Job: {i[1]:<10}')
    # finish loop here
    db.close

# 3rd category menu functions
def character_affiliation_menu():
    while True:
        try:
            affi = int(input("\nCharacter affiliation menu: \n\n 1.)  All characters and their affiliations (some will show up more than once)\n 2.)  Characters affiliated with the Armed Detective Agency \n 3.)  Characters affiliated with the Port Mafia\n 4.)  Characters affiliated with the Japanese government\n 5.)  Characters affiliated with the Japanese millitary\n 6.)  Characters affiliated with the Guild\n 7.)  Characters affiliated with Rats in the House of the Dead\n 8.)  Characters affiliated with the Decay of Angels\n 9.)  Characters affiliated with the Sheep\n 10.) Characters affiliated with the Transcendents\n 11.) Characters affiliated with Manhasset Security\n 12.) Characters affiliated with Mimic\n 13.) Characters affiliated with other organisations\n 14.) Unaffiliated characters\n 15.) Back to main menu\n"))
            if affi == 2:
                ada_character_affiliation()
            if affi == 15:
                bsd_main_menu()
                break
        except ValueError:
            print('Answer in numbers from 1-15 only please.\n')
    return


def character_inspo_menu():
    while True:
        try:
            inspo = int(input("The inspiration for characters menu: \n(read the bit of explanation about the series from the main menu for context) \n\n 1.) All characters with known inspirations from the real world \n 2.) Sort by the real-life authors that inspired the characters' death year\n 3.) Sort by the real-life authors that inspired the characters' birth year\n 4.) Back to main menu\n"))
            if inspo == 4:
                bsd_main_menu()
                break
        except ValueError:
            print('Answer in numbers from 1-4 only please.\n')
    return


# 2nd category menu functions
def bsd_backstory():
        print('\nBungo Stray Dogs is about...\n')
        while True:
            exit = input("Do you want to back to main menu? 'yes' or 'no' answers only please.\n")
            if exit == 'yes':
                bsd_main_menu()
                break
            if exit == 'no':
                exit_option()
                break
           
def bsd_character_menu_1():
    while True:
        try:
            first_characters_menu = int(input('\nCharacters menu:\n 1.) All characters \n 2.) Characters with abilities \n 3.) Sort by inspiration \n 4.) Sort by affiliation \n 5.) Sort by age \n 6.) Sort by gender \n 7.) Sort by status \n 8.) Sort by nationality \n 9.) Back to main menu\n\n'))
            if first_characters_menu == 1:
                all_characters()
            if first_characters_menu == 2:
                characters_with_abilities()
            if first_characters_menu == 3:
                character_inspo_menu()
            if first_characters_menu == 4:
                character_affiliation_menu()
            if first_characters_menu == 9:
                bsd_main_menu()
                break
        except ValueError:
            print('Answer in numbers from 1-9 only please.\n')
        return

# navigation main menu
def bsd_main_menu():
    while True:
        try:
            main_menu = int(input('\nMain menu: \n 1.) A bit about Bungo Stray Dogs before you get started. \n 2.) Characters database \n 3.) Exit menu \n \n'))
            if main_menu == 1:
                bsd_backstory()
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


