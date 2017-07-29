#!/bin/python3


from npc2 import *




# example code 
#        npc('name', 'species', 'career', 'NPC type')
pirate = npc('Todd Spunkle-Dinker','human','pirate', 'nemesis')



print("\n\n")
print("    Pirate Object Example       ")
print("--------------------------------")
print("Name:             ", pirate.name)
print("Species:          ", pirate.species)
print("Class:            ", pirate.npc_class)
print("Class Bonus:      ", "Some Bonus")
print("NPC Type:         ", pirate.npc_type)
print("NPC Rules:",pirate.rules(),"\n")
print("--------------------------------")
print("Characteristics:        ", pirate.characteristics())
print("--------------------------------")
print("General Skills:   ", pirate.general_skills())
print("Combat Skills:    ", pirate.combat_skills())
print("Knowledge Skills: ", pirate.knowledge_skills())
print("\n\n")








