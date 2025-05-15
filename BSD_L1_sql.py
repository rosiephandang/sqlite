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

def all_inspo():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT name, inspo FROM bsd_characters WHERE NOT inspo = 'unknown' ORDER BY name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nAll characters with known inspiration:\n')
    for character in results:
        print(f'Name: {character[0]:<36}Inspiration: {character[1]:<35}\n')
    # finish loop here
    db.close

# asking about the real death & birth years of inspo query functions
def inspo_birth_year_before():
    # docstring - print all outputs nicely
    bfr_birth = int(input('\nEnter a year: '))
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = 'SELECT name, inspo, birth_year, death_year FROM bsd_characters WHERE birth_year <= ? ORDER BY name ASC;'
    cursor.execute(sql,(bfr_birth,))
    results = cursor.fetchall()
    # loop through the results
    print(f'\nCharacters with authors (as their inspiration) born before {bfr_birth} are:')
    for i in results:
        print(f'Name: {i[0]:<35}Inspiration: {i[1]:<85}Birth year: {i[2]:<10}Death year: {i[3]}')
    # finish loop here
    db.close

def inspo_birth_year_after():
    # docstring - print all outputs nicely
    aft_birth = int(input('\nEnter a year: '))
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = 'SELECT name, inspo, birth_year, death_year FROM bsd_characters WHERE birth_year >= ? ORDER BY name ASC;'
    cursor.execute(sql,(aft_birth,))
    results = cursor.fetchall()
    # loop through the results
    print(f'\nCharacters with authors (as their inspiration) born after {aft_birth} are:')
    for i in results:
        print(f'Name: {i[0]:<35}Inspiration: {i[1]:<85}Birth year: {i[2]:<10}Death year: {i[3]}')
    # finish loop here
    db.close

def inspo_death_year_before():
    # docstring - print all outputs nicely
    bfr_death = int(input('\nEnter a year: '))
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = 'SELECT name, inspo, birth_year, death_year FROM bsd_characters WHERE death_year <= ? ORDER BY name ASC;'
    cursor.execute(sql,(bfr_death,))
    results = cursor.fetchall()
    # loop through the results
    print(f'\nCharacters with authors (as their inspiration) that died before {bfr_death} are:')
    for i in results:
        print(f'Name: {i[0]:<35}Inspiration: {i[1]:<85}Birth year: {i[2]:<10}Death year: {i[3]}')
    # finish loop here
    db.close

def inspo_death_year_after():
    # docstring - print all outputs nicely
    aft_death = int(input('\nEnter a year: '))
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = 'SELECT name, inspo, birth_year, death_year FROM bsd_characters WHERE death_year >= ? ORDER BY name ASC;'
    cursor.execute(sql,(aft_death,))
    results = cursor.fetchall()
    # loop through the results
    print(f'\nCharacters with authors (as their inspiration) that died after {aft_death} are:')
    for i in results:
        print(f'Name: {i[0]:<35}Inspiration: {i[1]:<85}Birth year: {i[2]:<10}Death year: {i[3]}')
    # finish loop here
    db.close

# asking character ages queries 

def below_age():
    # docstring - print all outputs nicely
    blw_age = int(input('\nEnter an age: '))
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = 'SELECT name, age, gender, status FROM bsd_characters WHERE age <= ? ORDER BY name ASC;'
    cursor.execute(sql,(blw_age,))
    results = cursor.fetchall()
    # loop through the results
    print(f'\nCharacters below {blw_age} are:')
    for i in results:
        print(f'Name: {i[0]:<35}Age: {i[1]:<10}Gender: {i[2]:<10}Status: {i[3]}')
    # finish loop here
    db.close

def above_age():
    # docstring - print all outputs nicely
    abv_age = int(input('\nEnter an age: '))
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = 'SELECT name, age, gender, status FROM bsd_characters WHERE age >= ? ORDER BY name ASC;'
    cursor.execute(sql,(abv_age,))
    results = cursor.fetchall()
    # loop through the results
    print(f'\nCharacters above {abv_age} are:')
    for i in results:
        print(f'Name: {i[0]:<35}Age: {i[1]:<10}Gender: {i[2]:<10}Status: {i[3]}')
    # finish loop here
    db.close

def age_10s():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT name, est_age, gender, status FROM bsd_characters WHERE est_age = '10s' ORDER BY name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nAll characters estimated to be in their teens:\n')
    for character in results:
        print(f'Name: {character[0]:<36}Gender: {character[2]:<75}Status: {character[3]}\n')
    # finish loop here
    db.close

def age_20s():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT name, est_age, gender, status FROM bsd_characters WHERE est_age = '20s' ORDER BY name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nAll characters estimated to be in their twenties:\n')
    for character in results:
        print(f'Name: {character[0]:<36}Gender: {character[2]:<75}Status: {character[3]}\n')
    # finish loop here
    db.close

def age_30s():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT name, est_age, gender, status FROM bsd_characters WHERE est_age = '30s' ORDER BY name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nAll characters estimated to be in their thirties:\n')
    for character in results:
        print(f'Name: {character[0]:<36}Gender: {character[2]:<75}Status: {character[3]}\n')
    # finish loop here
    db.close

def age_40s():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT name, est_age, gender, status FROM bsd_characters WHERE est_age = '40s' ORDER BY name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nAll characters estimated to be in their fourties:\n')
    for character in results:
        print(f'Name: {character[0]:<36}Gender: {character[2]:<75}Status: {character[3]}\n')
    # finish loop here
    db.close

def age_50s():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT name, est_age, gender, status FROM bsd_characters WHERE est_age = '50s' ORDER BY name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nAll characters estimated to be in their fifties:\n')
    for character in results:
        print(f'Name: {character[0]:<36}Gender: {character[2]:<75}Status: {character[3]}\n')
    # finish loop here
    db.close

def age_unknown():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT name, est_age, gender, status FROM bsd_characters WHERE est_age = '?' ORDER BY name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nAll characters with entirely unknown ages:\n')
    for character in results:
        print(f'Name: {character[0]:<36}Gender: {character[2]:<75}Status: {character[3]}\n')
    # finish loop here
    db.close

# character gender sort query functions
def female_characters():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT name, gender, job FROM bsd_characters WHERE gender = 'Female' ORDER BY name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nAll female characters:\n')
    for character in results:
        print(f'Name: {character[0]:<40}Gender: {character[1]:<15}Job: {character[2]}\n')
    # finish loop here
    db.close

def male_characters():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT name, gender, job FROM bsd_characters WHERE gender = 'Male' ORDER BY name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nAll male characters:\n')
    for character in results:
        print(f'Name: {character[0]:<40}Gender: {character[1]:<15}Job {character[2]}\n')
    # finish loop here
    db.close

def other_gender_characters():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT name, gender, job FROM bsd_characters WHERE gender = 'Other' ORDER BY name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nAll other gendered characters:\n')
    for character in results:
        print(f'Name: {character[0]:<40}Gender: {character[1]:<15}Job: {character[2]}\n')
    # finish loop here
    db.close

# character status sort query functions
def alive_characters():
     # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT name, status, job FROM bsd_characters WHERE status = 'Alive' ORDER BY name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nAll alive characters:\n')
    for character in results:
        print(f'Name: {character[0]:<40}Status: {character[1]:<15}Job: {character[2]}\n')
    # finish loop here
    db.close

def dead_characters():
     # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT name, status, job FROM bsd_characters WHERE status = 'Dead' ORDER BY name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nAll dead characters:\n')
    for character in results:
        print(f'Name: {character[0]:<40}Status: {character[1]:<15}Job: {character[2]}\n')
    # finish loop here
    db.close

def unknown_characters():
     # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT name, status, job FROM bsd_characters WHERE status = 'Unknown' ORDER BY name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nAll status unknown characters:\n')
    for character in results:
        print(f'Name: {character[0]:<40}Status: {character[1]:<15}Job: {character[2]}\n')
    # finish loop here
    db.close

# affiliation character query functions

def all_character_affiliation():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT bsd_characters.name, bsd_characters.job, affiliation.affiliation_name FROM bsd_characters JOIN character_affiliation ON bsd_characters.id = character_affiliation.character_id JOIN affiliation ON affiliation.affiliation_id = character_affiliation.affiliation_id ORDER BY bsd_characters.name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nAll characters and their affiliations:\n')
    for i in results:
        print(f'Name: {i[0]:<35}Job: {i[1]:<85}Affiliation: {i[2]}')
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
    print(f'\nCharacters affiliated with the Armed Detective Agency are:\n')
    for i in results:
        print(f'Name: {i[0]:<30}Job: {i[1]:<10}')
    # finish loop here
    db.close

def pm_character_affiliation():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT bsd_characters.name, bsd_characters.job, affiliation.affiliation_name FROM bsd_characters JOIN character_affiliation ON bsd_characters.id = character_affiliation.character_id JOIN affiliation ON affiliation.affiliation_id = character_affiliation.affiliation_id WHERE affiliation.affiliation_name = 'Port Mafia ' ORDER BY bsd_characters.name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nCharacters affiliated with the Port Mafia are:\n')
    for i in results:
        print(f'Name: {i[0]:<30}Job: {i[1]:<10}')
    # finish loop here
    db.close

def jpn_gov_character_affiliation():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT bsd_characters.name, bsd_characters.job, affiliation.affiliation_name FROM bsd_characters JOIN character_affiliation ON bsd_characters.id = character_affiliation.character_id JOIN affiliation ON affiliation.affiliation_id = character_affiliation.affiliation_id WHERE affiliation.affiliation_name = 'Japanese Government' ORDER BY bsd_characters.name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nCharacters affiliated with the Japanese government are:\n')
    for i in results:
        print(f'Name: {i[0]:<30}Job: {i[1]:<10}')
    # finish loop here
    db.close

def jpn_mltr_character_affiliation():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT bsd_characters.name, bsd_characters.job, affiliation.affiliation_name FROM bsd_characters JOIN character_affiliation ON bsd_characters.id = character_affiliation.character_id JOIN affiliation ON affiliation.affiliation_id = character_affiliation.affiliation_id WHERE affiliation.affiliation_name = 'Japanese Military' ORDER BY bsd_characters.name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nCharacters affiliated with the Japanese millitary are:\n')
    for i in results:
        print(f'Name: {i[0]:<30}Job: {i[1]:<10}')
    # finish loop here
    db.close

def guild_character_affiliation():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT bsd_characters.name, bsd_characters.job, affiliation.affiliation_name FROM bsd_characters JOIN character_affiliation ON bsd_characters.id = character_affiliation.character_id JOIN affiliation ON affiliation.affiliation_id = character_affiliation.affiliation_id WHERE affiliation.affiliation_name = 'The Guild' ORDER BY bsd_characters.name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nCharacters affiliated with the Guild are:\n')
    for i in results:
        print(f'Name: {i[0]:<30}Job: {i[1]:<10}')
    # finish loop here
    db.close

def rats_character_affiliation():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT bsd_characters.name, bsd_characters.job, affiliation.affiliation_name FROM bsd_characters JOIN character_affiliation ON bsd_characters.id = character_affiliation.character_id JOIN affiliation ON affiliation.affiliation_id = character_affiliation.affiliation_id WHERE affiliation.affiliation_name = 'Rats in the House of the Dead' ORDER BY bsd_characters.name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nCharacters affiliated with the Rats in the Housse of the Dead are:\n')
    for i in results:
        print(f'Name: {i[0]:<30}Job: {i[1]:<10}')
    # finish loop here
    db.close

def doa_character_affiliation():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT bsd_characters.name, bsd_characters.job, affiliation.affiliation_name FROM bsd_characters JOIN character_affiliation ON bsd_characters.id = character_affiliation.character_id JOIN affiliation ON affiliation.affiliation_id = character_affiliation.affiliation_id WHERE affiliation.affiliation_name = 'Decay of Angels' ORDER BY bsd_characters.name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nCharacters affiliated with the Decay of Angels are:\n')
    for i in results:
        print(f'Name: {i[0]:<30}Job: {i[1]:<10}')
    # finish loop here
    db.close

def sheep_character_affiliation():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT bsd_characters.name, bsd_characters.job, affiliation.affiliation_name FROM bsd_characters JOIN character_affiliation ON bsd_characters.id = character_affiliation.character_id JOIN affiliation ON affiliation.affiliation_id = character_affiliation.affiliation_id WHERE affiliation.affiliation_name = 'The Sheep' ORDER BY bsd_characters.name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nCharacters affiliated with The Sheep are:\n')
    for i in results:
        print(f'Name: {i[0]:<30}Job: {i[1]:<10}')
    # finish loop here
    db.close

def tran_character_affiliation():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT bsd_characters.name, bsd_characters.job, affiliation.affiliation_name FROM bsd_characters JOIN character_affiliation ON bsd_characters.id = character_affiliation.character_id JOIN affiliation ON affiliation.affiliation_id = character_affiliation.affiliation_id WHERE affiliation.affiliation_name = 'Transcendents ' ORDER BY bsd_characters.name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nCharacters affiliated with The Transcendents are:\n')
    for i in results:
        print(f'Name: {i[0]:<30}Job: {i[1]:<10}')
    # finish loop here
    db.close

def manh_character_affiliation():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT bsd_characters.name, bsd_characters.job, affiliation.affiliation_name FROM bsd_characters JOIN character_affiliation ON bsd_characters.id = character_affiliation.character_id JOIN affiliation ON affiliation.affiliation_id = character_affiliation.affiliation_id WHERE affiliation.affiliation_name = 'Manhasset Security' ORDER BY bsd_characters.name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nCharacters affiliated with Manhasset Security are:\n')
    for i in results:
        print(f'Name: {i[0]:<30}Job: {i[1]:<10}')
    # finish loop here
    db.close

def mimic_character_affiliation():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT bsd_characters.name, bsd_characters.job, affiliation.affiliation_name FROM bsd_characters JOIN character_affiliation ON bsd_characters.id = character_affiliation.character_id JOIN affiliation ON affiliation.affiliation_id = character_affiliation.affiliation_id WHERE affiliation.affiliation_name = 'Mimic' ORDER BY bsd_characters.name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nCharacters affiliated with Mimic are:\n')
    for i in results:
        print(f'Name: {i[0]:<30}Job: {i[1]:<10}')
    # finish loop here
    db.close

def other_character_affiliation():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT bsd_characters.name, bsd_characters.job, affiliation.affiliation_name FROM bsd_characters JOIN character_affiliation ON bsd_characters.id = character_affiliation.character_id JOIN affiliation ON affiliation.affiliation_id = character_affiliation.affiliation_id WHERE affiliation.affiliation_name = 'Order of the Clock Tower' OR affiliation.affiliation_name = 'The 7 Traitors' OR affiliation.affiliation_name = 'V' OR affiliation.affiliation_name = 'Zoopark' AND NOT affiliation.affiliation_name = 'Unafilliated' ORDER BY bsd_characters.name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nCharacters affiliated with other organisations are are:\n')
    for i in results:
        print(f'Name: {i[0]:<30}Job: {i[1]:<50}Affiliation: {i[2]}')
    # finish loop here
    db.close

def un_character_affiliation():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT bsd_characters.name, bsd_characters.job, affiliation.affiliation_name FROM bsd_characters JOIN character_affiliation ON bsd_characters.id = character_affiliation.character_id JOIN affiliation ON affiliation.affiliation_id = character_affiliation.affiliation_id WHERE affiliation.affiliation_name = 'Unafilliated' ORDER BY bsd_characters.name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nUnaffiliated characters are:\n')
    for i in results:
        print(f'Name: {i[0]:<40}Job: {i[1]:<10}')
    # finish loop here
    db.close

# nationality query sort functions
def jpn_characters():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT name, nationality, job FROM bsd_characters WHERE nationality = 'Japanese' ORDER BY name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nAll Japanese characters:\n')
    for character in results:
        print(f'Name: {character[0]:<40}Nationality: {character[1]:<25}Job: {character[2]}\n')
    # finish loop here
    db.close

def ame_characters():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT name, nationality, job FROM bsd_characters WHERE nationality = 'American' ORDER BY name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nAll American characters:\n')
    for character in results:
        print(f'Name: {character[0]:<40}Nationality: {character[1]:<25}Job: {character[2]}\n')
    # finish loop here
    db.close

def fre_characters():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT name, nationality, job FROM bsd_characters WHERE nationality = 'French' ORDER BY name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nAll French characters:\n')
    for character in results:
        print(f'Name: {character[0]:<40}Nationality: {character[1]:<25}Job: {character[2]}\n')
    # finish loop here
    db.close

def bri_characters():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT name, nationality, job FROM bsd_characters WHERE nationality = 'British' ORDER BY name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nAll British characters:\n')
    for character in results:
        print(f'Name: {character[0]:<40}Nationality: {character[1]:<25}Job: {character[2]}\n')
    # finish loop here
    db.close

def rus_characters():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT name, nationality, job FROM bsd_characters WHERE nationality = 'Russian' ORDER BY name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nAll Russian characters:\n')
    for character in results:
        print(f'Name: {character[0]:<40}Nationality: {character[1]:<25}Job: {character[2]}\n')
    # finish loop here
    db.close

def oth_nation_characters():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT name, nationality, job FROM bsd_characters WHERE NOT nationality = 'Japanese' AND NOT nationality = 'American' AND NOT nationality = 'French' AND NOT nationality = 'British' AND NOT nationality = 'Russian' AND NOT nationality = 'Unknown' ORDER BY name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nAll other nationalities (on on the previous menu) characters:\n')
    for character in results:
        print(f'Name: {character[0]:<40}Nationality: {character[1]:<25}Job: {character[2]}\n')
    # finish loop here
    db.close

def un_nation_characters():
    # docstring - print all outputs nicely
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT name, nationality, job FROM bsd_characters WHERE nationality = 'Unknown' ORDER BY name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through the results
    print(f'\nAll characters with unknown nationalities:\n')
    for character in results:
        print(f'Name: {character[0]:<40}Nationality: {character[1]:<25}Job: {character[2]}\n')
    # finish loop here
    db.close

# 4th category menu functions
def inspo_birth_year():
    while True:
        try:
            b_year = int(input('\nHow do you want to sort by birth year?\n 1.) Sort by before a year\n 2.) Sort by after a year\n 3.) Back to main menu\n\n'))
            if b_year == 1:
                inspo_birth_year_before()
            if b_year == 2:
                inspo_birth_year_after()
            if b_year == 3:
                bsd_main_menu()
                break
        except ValueError:
            print('Answer in numbers from 1-3 only please.\n')
    return

def inspo_death_year():
    while True:
        try:
            b_year = int(input('\nHow do you want to sort by death year?\n 1.) Sort by before a year\n 2.) Sort by after a year\n 3.) Back to main menu\n\n'))
            if b_year == 1:
                inspo_death_year_before()
            if b_year == 2:
                inspo_death_year_after()
            if b_year == 3:
                bsd_main_menu()
                break
        except ValueError:
            print('Answer in numbers from 1-3 only please.\n')
    return

def un_est_age():
    while True:
        try:
            est_age = int(input("\nHow do you want to sort the ages of the characters that haven't been explicitly stated?\n 1.) Characters estimated to be in their teens\n 2.) Characters estimated to be in their 20s\n 3.) Characters estimated to be in their 30s\n 4.) Characters estimated to be in their 40s\n 5.) Characters estimated to be in their 50s\n 6.) Characters with entirely unknown ages\n 7.) Back to main menu\n\n"))
            if est_age == 1:
                age_10s()
            if est_age == 2:
                age_20s()
            if est_age == 3:
                age_30s()
            if est_age == 4:
                age_40s()
            if est_age == 5:
                age_50s()
            if est_age == 6:
                age_unknown()
            if est_age == 7:
                bsd_main_menu()
                break
        except ValueError:
            print('Answer in numbers from 1-7 only please.\n')
    return


# 3rd category menu functions
def character_affiliation_menu():
    while True:
        try:
            affi = int(input("\nCharacter affiliation menu: \n\n 1.)  All characters and their affiliations (some will show up more than once)\n 2.)  Characters affiliated with the Armed Detective Agency \n 3.)  Characters affiliated with the Port Mafia\n 4.)  Characters affiliated with the Japanese government\n 5.)  Characters affiliated with the Japanese millitary\n 6.)  Characters affiliated with the Guild\n 7.)  Characters affiliated with Rats in the House of the Dead\n 8.)  Characters affiliated with the Decay of Angels\n 9.)  Characters affiliated with the Sheep\n 10.) Characters affiliated with the Transcendents\n 11.) Characters affiliated with Manhasset Security\n 12.) Characters affiliated with Mimic\n 13.) Characters affiliated with other organisations\n 14.) Unaffiliated characters\n 15.) Back to main menu\n\n"))
            if affi == 1:
                all_character_affiliation()
            if affi == 2:
                ada_character_affiliation()
            if affi == 3:
                pm_character_affiliation()
            if affi == 4:
                jpn_gov_character_affiliation()
            if affi == 5:
                jpn_mltr_character_affiliation()
            if affi == 6:
                guild_character_affiliation()
            if affi == 7:
                rats_character_affiliation()
            if affi == 8:
                doa_character_affiliation()
            if affi == 9:
                sheep_character_affiliation()
            if affi == 10:
                tran_character_affiliation()
            if affi == 11:
                manh_character_affiliation()
            if affi == 12:
                mimic_character_affiliation()
            if affi == 13:
                other_character_affiliation()
            if affi == 14:
                un_character_affiliation()
            if affi == 15:
                bsd_main_menu()
                break
        except ValueError:
            print('Answer in numbers from 1-15 only please.\n')
    return

def character_inspo_menu():
    while True:
        try:
            inspo = int(input("The inspiration for characters menu: \n(read the bit of explanation about the series from the main menu for context) \n\n 1.) All characters with known inspirations from the real world \n 2.) Sort by the real-life authors that inspired the characters' death year\n 3.) Sort by the real-life authors that inspired the characters' birth year\n 4.) Back to main menu\n\n Warning, 2 & 3 only works for characters that are inspired by actual authors. For more context, check out the background info about the series in the main menu.\n\n "))
            if inspo == 1:
                all_inspo()
            if inspo == 2:
                inspo_death_year()
            if inspo == 3:
                inspo_birth_year()
            if inspo == 4:
                bsd_main_menu()
                break
        except ValueError:
            print('Answer in numbers from 1-4 only please.\n')
    return

def character_age():
    while True:
        try:
            age = int(input('How do you want to sort by character age?\n\n 1.) Sort for characters below a certain age\n 2.) Sort for characters above a certain age\n 3.) Sort for characters with unknown ages\n 4.) Back to main menu\n\n'))
            if age == 1:
                below_age()
            if age == 2:
                above_age()
            if age == 3:
                un_est_age()
            if age == 4:
                bsd_main_menu()
        except ValueError:
            print('Answer in numbers from 1-4 only please.\n')

def character_gender():
    while True:
        try:
            gender = int(input('How do you want to sort by character gender?\n\n 1.) Sort for female characters\n 2.) Sort for male characters\n 3.) Sort for other gender characters\n 4.) Back to main menu\n\n'))
            if gender == 1:
                female_characters()
            if gender == 2:
                male_characters()
            if gender == 3:
                other_gender_characters()
            if gender == 4:
                bsd_main_menu()
        except ValueError:
            print('Answer in numbers from 1-4 only please.\n')

def character_status():
    while True:
        try:
            status = int(input('How do you want to sort by character status? Warning, spoilers ahead.\n\n 1.) Sort for alive characters\n 2.) Sort for dead characters\n 3.) Sort for status curently unknown characters\n 4.) Back to main menu\n\n'))
            if status == 1:
                alive_characters()
            if status == 2:
                dead_characters()
            if status == 3:
                unknown_characters()
            if status == 4:
                bsd_main_menu()
        except ValueError:
            print('Answer in numbers from 1-4 only please.\n')

def character_nationality():
    while True:
        try:
            nation = int(input('How do you want to sort by character nationality? \n\n 1.) Sort for Japanese characters\n 2.) Sort for American characters\n 3.) Sort for French characters\n 4.) Sort for British characters\n 5.) Sort for Russian characters\n 6.) Sort for other nationality characters\n 7.) Sort for unknown nationality characters\n 8.) Back to main menu\n\n'))
            if nation == 1:
                jpn_characters()
            if nation == 2:
                ame_characters()
            if nation == 3:
                fre_characters()
            if nation == 4:
                bri_characters()
            if nation == 5:
                rus_characters()
            if nation == 6:
                oth_nation_characters()
            if nation == 7:
                un_nation_characters()
            if nation == 8:
                bsd_main_menu()
        except ValueError:
            print('Answer in numbers from 1-8 only please.\n')

# 2nd category menu functions
def bsd_backstory():
        print("\nBungo Stray Dogs is about an orphan who finds out he's a man-eating tiger after saving a man from drowning at the ripe old age of 18. The man turns out to be a detective, \nand the orphan now finds himself with a job. Now, he has to fight American capitalists and Russian terrorists. \n\nThat's what the summary says, at least. \n\nI would say it's a seinen series that mixes humor and tragedies really well, and the characters are very well written (the mimimal fanservice is a bonus). \n\nThe characters are basically literacy references. Fyodor Dostoyevsky, Dazai Osamu, Edgar Allan Poe, Louisa May Alcott, etc. Very famous names in old classics, \nand they are all characters in this series, with their 'abilities' being created as an interpretation of some of their most famous works. \nThe supporting cast is also made up of characters that show up in these authors' books.\n\nThe series is still ongoing, and so this is only accurate as of May 2025. \n")
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
            if first_characters_menu == 5:
                character_age()
            if first_characters_menu == 6:
                character_gender()
            if first_characters_menu == 7:
                character_status()
            if first_characters_menu == 8:
                character_nationality()
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
    return
        

# intro main menu function
while True:
    intro = input("Enter 'yes' to keep going, or 'no' to stop:\n")
    if intro == 'yes':
        bsd_main_menu()
    if intro == 'no':
        exit_option()
        break


