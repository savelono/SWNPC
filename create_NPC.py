#!/bin/python3


from swnpc2 import *




# example code 
#        npc('name', 'species', 'career', 'NPC type')
pirate = npc('Wu Tang Clan Member','human - corelian','pirate', 'minion')



print("\n\n")
print("    Pirate Object Example       ")
print("--------------------------------")
print("Name:              ", pirate.name)
print("Species:           ", pirate.species)
print("Class:             ", pirate.npc_class)
print("Talents:           ", pirate.talents())
print("NPC Type:          ", pirate.npc_type)
print("NPC Rules:         ", pirate.rules(),"\n")
print("--------------------------------")
print("Characteristics:   ", pirate.characteristics())
print("--------------------------------")
print("General Skills:    ", pirate.general_skills())
print("Combat Skills:     ", pirate.combat_skills())
print("Knowledge Skills:  ", pirate.knowledge_skills())
print()
print()
print("Armor:             ", pirate.armor())
print("Weapons:           ", pirate.equipment())
print("\n\n")





