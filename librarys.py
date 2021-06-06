Standard_weapons = {'Standard Issue Hand Cannon':
                        {'dmg':10, 'desc': 'A standard, legion issue hand cannon', 'modifiers': {'perks': ['None']}, 'range': 'medium to close', 'archetype': 'Hand Cannon'},
                    'Standard Issue Shotgun':
                        {'dmg': 20, 'desc': 'A standard, legion issue shotgun',  'modifiers': {'perks': ['None']}, 'range': 'close', 'archetype': 'Shotgun'},
                    'Standard Issue Assault Rifle':
                        {'dmg': 5, 'desc': 'A standard, legion issue assault rifle',  'modifiers': {'perks': ['Yes', 'auto']}, 'range': 'medium', 'archetype': 'Assault Rifle'},
                    "Soldier Sword":
                        {'dmg': 8, 'desc': "A standard soldier's one-handed sword", 'modifiers': {'perks': ['None']}, 'range': 'melee', 'archetype': 'Sword'},
                    "Soldier Shield":
                        {"dmg": None, 'desc': "A standard soldier's bronze shield", 'modifiers': {'perks': ['None']}, 'range': 'defensive', 'archetype': 'Shield'},
                    "Soldier War Hammer":
                        {"dmg": 15, 'desc': "A standard soldier's two-handed war hammer", 'modifiers': {'perks': ['None']}, 'range': 'melee', 'archetype': 'War Hammer'},
                    "Rusted Dagger":
                        {'dmg': 6, 'desc': "A rusted steel dagger", 'modifiers': {'perks': ['None']}, 'range': 'melee', 'archetype': 'Dagger'},
                    "Thief Cloak":
                        {'dmg': 'Increases by x1.5', 'desc': 'A cloak that decreases your profile and increases your stealth', 'modifiers': {'perks': ['None']}, 'range': 'any', 'archetype': 'cloak'},
                    "Thief Smoke Bomb":
                        {'dmg': 'None', 'desc': 'A smoke bomb that allows you to disengage in battles without any risk', 'modifiers': {'perks': ['None']}, 'range': 'any', 'archetype': 'smoke bomb'}
                    }

Warlock_weapons = {"Otherworldly Pact":
                       {'dmg':None, 'desc': "A pact with a being from a higher plane of existence", 'modifiers': {'perks': ['Yes', 'magic']}, 'range': 'any', 'archetype': 'Pact'},
                   "Novice Spellbook":
                       {'dmg': 'depends on spell', 'desc': "A warlock novice's spellbook, contains all known low level spells and spells included with pacts", 'modifiers': {'perks': ['Yes', 'magic']}, 'range': 'any', 'archetype': 'Spellbook'},
                   "Novice Alchemy Pack":
                       {'dmg': 'depends on potion', 'desc': "A warlock novice's alchemy pack, allows you to create special potions mid-battle", 'modifiers': {'perks': ['Yes', 'magic']}, 'range': 'any', 'archetype': 'Backpack'}}


pact_beings = {'Minor Hellspawn':
                   {'spells': ['Hellfire Blast', 'Cauterize'], 'desc': 'A being that collectively consists of the minor demons of the Underworld'},
               'Styx':
                   {'spells': ['Stygian Fire', 'Styx Dip'], 'desc': 'The goddess of the River Styx, capable of painfully burning away your very essence or making you invulnerable'},
               'Asclepius':
                   {'spells': ['Heal', 'Venom Sting'], 'desc': 'The god of healing, allows you to heal you or your allies, or sting your enemies with venom'}
               }