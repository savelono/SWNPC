#!/bin/python3


from swnpc2 import *




# Dictionary for Species options
# notes - abilities.keys() taken from swnpc2 module
# these vaiables are for making a dictionary of menu
# optins.
#--------------------------------------------
# define list in alphabetical order
speciesL = sorted( [ create_species for create_species in abilities.keys() ] )

# define length
speciesN = [ species_number for species_number in range(1,len(speciesL)+1) ]

# assign each to dictionary with zip
species_menu_items = dict(zip(speciesN,speciesL))
#-------------------------------------------

#=============================================================

# Dictionary for career options
# notes - abilities.keys() taken from swnpc2 module
# these vaiables are for making a dictionary of menu
# optins.
#--------------------------------------------
# define list in alphabetical order
careerL = sorted( [ careers for careers in career.keys() ] )

# define length
careerN = [ career_number for career_number in range(1,len(careerL)+1) ]

# assign each to dictionary with zip
career_menu_items = dict(zip(careerN,careerL))

 


print('========================================')
print('Python interactive NPC builder')
print('========================================')
print("     _______..___________.     ___      .______      ____    __    ____      ___      .______           _______.")
print("    /       ||           |    /   \     |   _  \     \   \  /  \  /   /     /   \     |   _  \         /       |")
print("   |   (----``---|  |----`   /  ^  \    |  |_)  |     \   \/    \/   /     /  ^  \    |  |_)  |       |   (----`")
print("    \   \        |  |       /  /_\  \   |      /       \            /     /  /_\  \   |      /         \   \    ")
print(".----)   |       |  |      /  _____  \  |  |\  \----.   \    /\    /     /  _____  \  |  |\  \----..----)   |   ")
print("|_______/        |__|     /__/     \__\ | _| `._____|    \__/  \__/     /__/     \__\ | _| `._____||_______/    ")
print()
print()


#    questions
#-------------------------------
# - number of NPC's
# - type(minion,rival, or nemisis)
# - species
# - name
#


while True:

# Select number of NPC's to create

    create_npc_name = str(input("Please enter name of NPC: "))

    create_npc_group = str(input("Please enter name of NPC Affiliation: "))

    break

while True:

    try:
        numbernpcs = int(input("Please enter number of NPC\'s: "))

    except ValueError:
        print("Please type whole number greater than 0")
        continue

# check if user input is greater than one
    if numbernpcs < 1 or numbernpcs > 100:
        print('NPC\'s must be greater than one or fewer than a hundred')
        continue

    else:
        break
        
#---------------------------------------------

while True:

# Select NPC Type

    try:
        create_npc_type = int(input("Please enter NPC Type: [1] for Minion | [2] for Rival | or [3] for Nemisis: "))

    except ValueError:
        print("Please select an option by number from the list")
        continue


# check if user input is between 1-3
    if create_npc_type == 1:
        create_npc_type = 'minion'
        break

    elif create_npc_type == 2:
        create_npc_type = 'rival'
        break

    elif create_npc_type == 3:
        create_npc_type = 'nemesis'
        break

    else:
        print("Please select option 1-3 for NPC type")
        continue

#-------------------------------------------

# pull species list into a dictionary of options

print('\n',"species list")
print("--------------")

for i in species_menu_items.items():
    print(str(i).replace('(','[').replace(')','').replace(',',']'))

print()


while True:

# select species

    try:
        create_npc_species = int(input("Please enter number for species type from list above: "))

    except ValueError:
        print("Please type whole number greater than 0")
        continue

    if create_npc_species < 1 or create_npc_species > len(abilities.keys()):
        print("For species type please select a number from the above list")
        continue

    else:
        break


# Pull Career choices

print('\n\n',"Career list")
print("--------------")

for i in career_menu_items.items():
    print(str(i).replace('(','[').replace(')','').replace(',',']'))

print()

while True:

# Select career
    try:
        create_npc_career = int(input("Please enter number for career type from list above: "))

    except ValueError:
        print("Please type whole number greater than 0")
        continue

    if create_npc_career < 1 or create_npc_career > len(abilities.keys()):
        print("For species type please select a number from the above list")
        continue

    else:
        break

#==================================================
print()

def generate_npcs(name,species,career,npc_type,qty,affiliation):

# example code 
#        npc('name', 'species', 'career', 'NPC type')
    sw_npc = npc(name,species,career, npc_type)

# Auto increment
    x = 0

    for npcs in range(0,qty):

        x += 1

        print("\n\n")
        print("    SW the RPG NPC #{}      ".format(x))
        print("--------------------------------")
        print("Name:              ", sw_npc.name)
        print("Afilliation:       ", affiliation)
        print("Species:           ", sw_npc.species)
        print("Class:             ", sw_npc.npc_class)
        print("Talents:           ", sw_npc.talents())
        print("NPC Type:          ", sw_npc.npc_type)
        print("NPC Rules:         ", sw_npc.rules(),"\n")
        print("--------------------------------")
        print("Characteristics:   ", sw_npc.characteristics())
        print("--------------------------------")
        print("General Skills:    ", sw_npc.general_skills())
        print("Combat Skills:     ", sw_npc.combat_skills())
        print("Knowledge Skills:  ", sw_npc.knowledge_skills())
        print()
        print()
        print("Armor:             ", sw_npc.armor())
        print("Weapons:           ", sw_npc.equipment())
        print("\n\n")




generate_npcs(create_npc_name,species_menu_items[create_npc_species],career_menu_items[create_npc_career],create_npc_type,numbernpcs,create_npc_group)
