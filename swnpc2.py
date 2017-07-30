#!/bin/python3

import random


# species:[ [ Brawn, Agility, Intellect, Cunning, Willpower, Presence, Wound, Strain ],
#           [ Wound threshhold modifier, Strain threshold modifer ], [ 'Additional species notes' ] ]
abilities = { 'human' :[ [2,2,2,2,2,2,10,10], ['Brawn', 'Willpower'], [] ],
              'keldor':[ [1,2,2,2,3,2,10,10], ['Brawn', 'Willpower'] ],
              'arcona':[ [1,2,2,2,3,2,10,10], ['Brawn', 'Willpower'] ],
              'gank'  :[ [2,2,2,2,2,2,10,10], ['Brawn', 'Willpower'] ],
              'wookie':[ [4,2,2,2,1,2,14,12], ['Brawn', 'Willpower'] ] }


# NPC class modifiers
# {career: [ [ ability modifiers ], [ skills - gen, com, know ], [ equipment ], [ talent/bonus ] ]} 

career = { 'pirate'       :[ [0,0,0,0,0,0,0,0], [2,3,1], ["Some equipment", "and some other equipment"], [] ], 
           'trooper'      :[ [0,0,0,0,0,0,0,0], [3,3,1], ["Some equipment", "and some other equipment"], [] ],
           'monk'         :[ [0,0,0,0,0,0,0,0], [3,3,1], ["Some equipment", "and some other equipment"], [] ],
           'bounty hunter':[ [0,0,0,0,0,0,0,0], [3,3,1], ["Some equipment", "and some other equipment"], [] ] }


# NPC type
#                type     : [ ["notes and rules"], [characteristic modifiers], [bonus skills] ]

type_rules = { 'minion'   : [ ["Does not suffer strain or posess skills.",  "They can fight as a group and be killed by crits."] ],
               'rival'    : [ ["Will Die after exceeding wound threshold.", "Suffers wounds for strain."], [0,0,0,0,0,0,4,4], [1,0,0] ],
               'nemesis'  : [ ["Standard Rules."], [1,1,1,1,1,1,8,8], [2,1,1] ] }




# Skills
general_skills = ( 'Astrogation (Int)',
                   'Athletics (Br)',
                   'Charm (Pr)',
                   'Coercion (Will)',
                   'Computers (Int)',
                   'Cool (Pr)',
                   'Coordination (Ag)',
                   'Deception (Cun)',
                   'Discipline (Will)',
                   'Leadership (Pr)',
                   'Mechanics (Int)',
                   'Medicine (Int)',
                   'Negotiaion (Pr)',
                   'Perception (Cun)',
                   'Piloting – Planetary (Ag)',
                   'Piloting – Space (Ag)',
                   'Resilience (Br)',
                   'Skulduggery (Cun)',
                   'Stealth (Ag)',
                   'Streetwise (Cun)',
                   'Survival (Cun)',
                   'Vigilance (Will)' )


combat_skills = ( 'Brawl (Br)',
                  'Gunnery (Ag)',
                  'Melee (Br)',
                  'Ranged – Light (Ag)',
                  'Ranged – Heavy (Ag)' )



knowledge_skills = ( 'Core Worlds (Int)',
                     'Education (Int)',
                     'Lore (Int)',
                     'Outer Rim (Int)',
                     'Underworld (Int)',
                     'Warfare (Int)',
                     'Xenology (Int)' )






class npc():

    def __init__(self, name, species, npc_class, npc_type):
        self.name = name
        self.species = species
        self.npc_class = str(npc_class)
        if npc_type == 'minion' or npc_type == 'rival' or npc_type == 'nemesis':
            self.npc_type = npc_type
        else:
            print('\n', "Must choose 'minion', 'rival', or 'nemeses'.",'\n\n')
            print(" Example calling npc object: npc('Duke Skyhawker', 'human', 'pirate', 'rival')", '\n')
            raise SystemExit

#---------------------------------------
    def characteristics(self):
        base_abilities = abilities[self.species][0]
        ability_list = [ 'Brawn', 'Agility', 'Intellect', 'Cunning', 'Willpower', 'Presence', 'Wound', 'Strain' ]
        ability_total = dict(zip(ability_list, base_abilities))
        ability_total['Brawn'] += career[self.npc_class][0][0]     + type_rules[self.npc_type][1][0]
        ability_total['Agility'] += career[self.npc_class][0][1]   + type_rules[self.npc_type][1][1]
        ability_total['Intellect'] += career[self.npc_class][0][2] + type_rules[self.npc_type][1][2]
        ability_total['Cunning'] += career[self.npc_class][0][3]   + type_rules[self.npc_type][1][3]
        ability_total['Willpower'] += career[self.npc_class][0][4] + type_rules[self.npc_type][1][4]
        ability_total['Presence'] += career[self.npc_class][0][5]  + type_rules[self.npc_type][1][5]
        ability_total['Wound'] += career[self.npc_class][0][6]     + type_rules[self.npc_type][1][6]
        ability_total['Strain'] += career[self.npc_class][0][7]    + type_rules[self.npc_type][1][7]

        return ability_total

#----------------------------------------

    def general_skills(self):
        if self.npc_type == 'minion':
            skill_limit = 2
        elif self.npc_type == 'rival':
            skill_limit = 3
        elif self.npc_type == 'nemesis':
            skill_limit = 4

        try:
            qty = career[self.npc_class][1][0] + type_rules[self.npc_type][2][0]
            return dict(zip(random.sample(general_skills,qty),[(random.randint(0,skill_limit) + 1) for number in range(1,qty + 1)]))
        except ValueError:
            return "Max amount of knowledge skills is 22"
#----------------------------------------

    def combat_skills(self):
        if self.npc_type == 'minion':
            skill_limit = 2
        elif self.npc_type == 'rival':
            skill_limit = 3
        elif self.npc_type == 'nemesis':
            skill_limit = 4

        try:
            qty = career[self.npc_class][1][1] + type_rules[self.npc_type][2][1]
            return dict(zip(random.sample(combat_skills,qty),[(random.randint(0,skill_limit) + 1) for number in range(1,qty + 1)]))
        except ValueError:
            return "Max amount of knowledge skills is 5"

#----------------------------------------

    def knowledge_skills(self):
        if self.npc_type == 'minion':
            skill_limit = 2
        elif self.npc_type == 'rival':
            skill_limit = 3
        elif self.npc_type == 'nemesis':
            skill_limit = 4

        try:
            qty = career[self.npc_class][1][2] + type_rules[self.npc_type][2][2]
            return dict(zip(random.sample(knowledge_skills,qty),[(random.randint(0,skill_limit) + 1) for number in range(1,qty + 1)]))
        except ValueError:
            return "Max amount of knowledge skills is 7"

#-----------------------------------------

    def rules(self):
        return type_rules[self.npc_type][0]


