# import discord
from keep_alive import keep_alive
from discord.ext import commands
import time
import sqlite3
from librarys import Standard_weapons, pact_beings, Warlock_weapons
from funcs import insert_weapon

bot = commands.Bot(command_prefix='!')
conn = sqlite3.connect('users.db')
c = conn.cursor()

start_rpg = False
waiting_for_reply = False
battle = False


@bot.command(name='start_rpg')
async def start_rpg(ctx):
    global start_rpg, waiting_for_reply, battle

    def check(m):
        return m.author == ctx.author

    time.sleep(1)
    await ctx.author.send(
        'This will create a new character for the rpg game. Are you sure you want to do this? y/n (If you want to resume with an existing character, use the command: !resume_rpg)')
    waiting_for_reply = True
    while waiting_for_reply:
        msg = await bot.wait_for('message', check=check)
        if msg and msg.content.lower() == 'y':
            start_rpg = True
            waiting_for_reply = False
        elif msg and msg.content.lower() == 'n':
            time.sleep(1)
            await ctx.author.send("Ok. If you want to resume with an existing character, use the command: !resume_rpg")
            waiting_for_reply = False
        else:
            time.sleep(1)
            await ctx.author.send('That is not a valid option. Try again with y or n')
    while start_rpg:
        time.sleep(1)
        await ctx.author.send('Enter a username for your character (Alphabetic characters only):')
        usrnam = await bot.wait_for('message', check=check)
        query = 'CREATE TABLE IF NOT EXISTS {}(level INTEGER, location TEXT, packs TEXT, class TEXT, money INTEGER)'.format(
            usrnam.content)
        c.execute(query)
        conn.commit()
        query = 'CREATE TABLE IF NOT EXISTS {}(weapon TEXT)'.format(usrnam.content + '_weapons')
        c.execute(query)
        conn.commit()
        query = "CREATE TABLE IF NOT EXISTS {}_chars(charnum INTEGER)".format(usrnam.content)
        c.execute(query)
        conn.commit()
        time.sleep(1)
        await ctx.author.send('Pick a **class** for your character:')
        time.sleep(1)
        await ctx.author.send(
            '**Gunslinger:** Elite marksmen with an increased affinity for firearms and increased accuracy with ranged weapons')
        time.sleep(1)
        await ctx.author.send(
            '**Warlock**: Master sorcerers with the ability to wield spells, which other classes may not use, and increased potion potency and holding capacity')
        time.sleep(1)
        await ctx.author.send(
            '**Titan**: Heavily armored warriors with an increased affinity for ranged weapons and an increased armor potency')
        time.sleep(1)
        await ctx.author.send(
            '**Rogue**: Stealthy warriors that have an increased affinity for stealth weapons and increased sneak capacity')
        waiting_for_reply = True
        while waiting_for_reply:
            time.sleep(1)
            await ctx.author.send('**Input your choice:**')
            player_class = await bot.wait_for('message', check=check)
            if player_class and player_class.content.lower() == 'gunslinger':
                time.sleep(1)
                await ctx.author.send('You picked the **Gunslinger** class')
                time.sleep(1)
                await ctx.author.send('These are your starting weapons:')
                time.sleep(1)
                await ctx.author.send(
                    '**Standard Issue Hand Cannon**: ' + Standard_weapons['Standard Issue Hand Cannon']['desc'])
                time.sleep(1)
                await ctx.author.send(
                    '**Standard Issue Shotgun**: ' + Standard_weapons['Standard Issue Shotgun']['desc'])
                time.sleep(1)
                await ctx.author.send(
                    '**Standard Issue Assault Rifle**: ' + Standard_weapons['Standard Issue Assault Rifle']['desc'])
                time.sleep(1)
                await ctx.author.send(
                    '**tip**: If in-game options have letters in front of them (A:, B:, C:, etc.), the the bot will only accept the letter as a valid input. Failure in inputting an option correctly may result in a game crash and lose all your progress.')
                query = "INSERT INTO {} VALUES(1, 'ruins', 'none', 'Gunslinger', 0)".format(usrnam.content)
                c.execute(query)
                conn.commit()
                query = "INSERT INTO {}_weapons VALUES('Standard Issue Hand Cannon')".format(usrnam.content)
                c.execute(query)
                conn.commit()
                query = "INSERT INTO {}_weapons VALUES('Standard Issue Shotgun')".format(usrnam.content)
                c.execute(query)
                conn.commit()
                query = "INSERT INTO {}_weapons VALUES('Standard Issue Assault Rifle')".format(usrnam.content)
                c.execute(query)
                conn.commit()
                time.sleep(1)
                await ctx.author.send('**Input anything to continue**')
                msg = await bot.wait_for('message', check=check)
                waiting_for_reply = False
            elif player_class and player_class.content.lower() == 'warlock':
                time.sleep(1)
                await ctx.author.send('You picked the **Warlock** class. These are your starting items:')
                time.sleep(1)
                await ctx.author.send('**Otherworldly Pact**: ' + Warlock_weapons['Otherworldly Pact']['desc'])
                time.sleep(1)
                await ctx.author.send("**Novice's Spellbook**: " + Warlock_weapons['Novice Spellbook']['desc'])
                time.sleep(1)
                await ctx.author.send("**Novice's Alchemy Pack**: " + Warlock_weapons['Novice Alchemy Pack']['desc'])
                time.sleep(1)
                await ctx.author.send('**Input anything to continue**:')
                msg = await bot.wait_for('message', check=check)
                time.sleep(1)
                await ctx.author.send('**You need to choose a being to forge a pact with**: ')
                time.sleep(1)
                await ctx.author.send('A: **Minor Hellspawn**: ' + pact_beings['Minor Hellspawn']['desc'])
                time.sleep(1)
                await ctx.author.send('B: **Styx**: ' + pact_beings['Styx']['desc'])
                time.sleep(1)
                await ctx.author.send('C: **Asclepius**: ' + pact_beings['Asclepius']['desc'])
                time.sleep(1)
                msg = await bot.wait_for('message', check=check)
                if msg and msg.content.lower() == 'a':
                    pact_being = 'Minor Hellspawn'
                elif msg and msg.content.lower() == 'b':
                    pact_being = 'Styx'
                elif msg and msg.content.lower() == 'c':
                    pact_being = 'Asclepius'
                query = "INSERT INTO {} VALUES(1, 'ruins', 'none', 'Warlock', 0)".format(usrnam.content)
                c.execute(query)
                conn.commit()
                query = "INSERT INTO {}_weapons VALUES('Otherworldly Pact({})')".format(usrnam.content, pact_being)
                c.execute(query)
                conn.commit()
                query = "INSERT INTO {}_weapons VALUES('Novice Spellbook')".format(usrnam.content)
                c.execute(query)
                conn.commit()
                query = "INSERT INTO {}_weapons VALUES('Novice Alchemy Pack')".format(usrnam.content)
                c.execute(query)
                conn.commit()
                await ctx.author.send('**Input anything to continue**')
                msg = await bot.wait_for('message', check=check)
                waiting_for_reply = False
            elif player_class and player_class.content.lower() == 'titan':
                time.sleep(1)
                await ctx.author.send('You picked the **Titan** class')
                time.sleep(1)
                await ctx.author.send('These are your starting weapons:')
                time.sleep(1)
                await ctx.author.send("**Soldier's Sword**: " + Standard_weapons["Soldier Sword"]['desc'])
                time.sleep(1)
                await ctx.author.send("**Soldier's Shield**: " + Standard_weapons['Soldier Shield']['desc'])
                time.sleep(1)
                await ctx.author.send("**Soldier's War Hammer**: " + Standard_weapons['Soldier War Hammer']['desc'])
                time.sleep(1)
                await ctx.author.send(
                    '**tip**: If in-game options have letters in front of them (A:, B:, C:, etc.), the the bot will only accept the letter as a valid input. Failure in inputting an option correctly may result in a game crash and lose all your progress.')
                query = "INSERT INTO {} VALUES(1, 'ruins', 'none', 'Titan', 0)".format(usrnam.content)
                c.execute(query)
                conn.commit()
                query = "INSERT INTO {}_weapons VALUES('Soldier Sword')".format(usrnam.content)
                c.execute(query)
                conn.commit()
                query = "INSERT INTO {}_weapons VALUES('Soldier Shield')".format(usrnam.content)
                c.execute(query)
                conn.commit()
                query = "INSERT INTO {}_weapons VALUES('Soldier War Hammer')".format(usrnam.content)
                c.execute(query)
                conn.commit()
                await ctx.author.send('**Input anything to continue**')
                msg = await bot.wait_for('message', check=check)
                waiting_for_reply = False
            elif player_class and player_class.content.lower() == 'rogue':
                time.sleep(1)
                await ctx.author.send('You picked the **Rogue** class')
                time.sleep(1)
                await ctx.author.send('These are your starting weapons:')
                time.sleep(1)
                await ctx.author.send("**Rusted Dagger**: " + Standard_weapons["Rusted Dagger"]['desc'])
                time.sleep(1)
                await ctx.author.send("**Thief's Cloak**: " + Standard_weapons['Thief Cloak']['desc'])
                time.sleep(1)
                await ctx.author.send("**Thief's Smoke Bomb**: " + Standard_weapons['Thief Smoke Bomb']['desc'])
                time.sleep(1)
                await ctx.author.send(
                    '**tip**: If in-game options have letters in front of them (A:, B:, C:, etc.), the the bot will only accept the letter as a valid input. Failure in inputting an option correctly may result in a game crash and lose all your progress.')
                query = "INSERT INTO {} VALUES(1, 'ruins', 'none', 'Rogue', 0)".format(usrnam.content)
                c.execute(query)
                conn.commit()
                query = "INSERT INTO {}_weapons VALUES('Rusted Dagger')".format(usrnam.content)
                c.execute(query)
                conn.commit()
                query = "INSERT INTO {}_weapons VALUES('Thief Cloak')".format(usrnam.content)
                c.execute(query)
                conn.commit()
                query = "INSERT INTO {}_weapons VALUES('Thief Smoke Bomb')".format(usrnam.content)
                c.execute(query)
                conn.commit()
                await ctx.author.send('**Input anything to continue**')
                msg = await bot.wait_for('message', check=check)
                waiting_for_reply = False
            else:
                time.sleep(1)
                await ctx.author.send(
                    'That is not a valid option. (Enter the full name of the class with correct spelling and input it)')
        time.sleep(1)
        await ctx.author.send(
            "**You wake up at the ruins of a Greek village. You have no recollection of anything; how you got here, what this place is. All you know is that something is wrong and all you have are your weapons.**")
        time.sleep(1)
        await ctx.author.send('**Input anything to continue**')
        msg = await bot.wait_for('message', check=check)
        time.sleep(1)
        await ctx.author.send("What do you want to do now?")
        time.sleep(1)
        await ctx.author.send("**Choices: ** ")
        time.sleep(1)
        await ctx.author.send("**A: Take a look around** ")
        time.sleep(1)
        await ctx.author.send("**B: Head out of the building**")
        time.sleep(1)
        waiting_for_reply = True
        while waiting_for_reply:
            await ctx.author.send('**Input your choice:**')
            msg = await bot.wait_for('message', check=check)
            if msg and msg.content.lower() == 'a':
                await ctx.author.send('You find a pouch of coins. It contains **15** drachma')
                player_money = 0
                player_money += 15
                query = "UPDATE {} SET money = {} WHERE class='{}'".format(usrnam.content, player_money,
                                                                           player_class.content)
                c.execute(query)
                conn.commit()
                time.sleep(1)
                await ctx.author.send(
                    'You have searched everywhere in the building. There is nothing else to find here. You head out of the building.')
                time.sleep(1)
                await ctx.author.send(
                    "You see an old man sitting on a half-demolished bench outside. He smiles when he sees you. What do you want to do now?")
                time.sleep(1)
                await ctx.author.send("**Choices: **")
                time.sleep(1)
                await ctx.author.send("**A: Talk to the man** ")
                time.sleep(1)
                await ctx.author.send("**B: Kill the man**")
                waiting_for_reply = False
            elif msg and msg.content.lower() == 'b':
                await ctx.author.send(
                    "You see an old man sitting on a half-demolished bench outside. He smiles when he sees you. What do you want to do now?")
                time.sleep(1)
                await ctx.author.send("**Choices: **")
                time.sleep(1)
                await ctx.author.send("**A: Talk to the man** ")
                time.sleep(1)
                await ctx.author.send("**B: Kill the man**")
                waiting_for_reply = False
            else:
                time.sleep(1)
                await ctx.author.send('That is not a valid option. Try again with a or b.')
        waiting_for_reply = True
        while waiting_for_reply:
            time.sleep(1)
            await ctx.author.send('**Input your choice**')
            msg = await bot.wait_for('message', check=check)
            if msg and msg.content.lower() == 'a':
                await ctx.author.send("**You approach the man. He goves you a rare pepe. Be very happe**")
                query = "INSERT INTO {}_weapons VALUES('RARE PEPE WAO')".format(usrnam.content)
                c.execute(query)
                conn.commit()
                waiting_for_reply = False
            if msg and msg.content.lower() == 'b':
                await ctx.author.send("**You have entered a battle with old man**!")
                time.sleep(1)
                await ctx.author.send(
                    "To choose a weapon at the start of any battle, enter the number in front of it at the start of the battle!")
                time.sleep(1)
                battle = True
                while battle:
                    player_health = 100
                    enemy_health = 10
                    await ctx.author.send("**Choose a weapon now to start the battle!**")
                    time.sleep(1)
                    query = 'SELECT * FROM {}_weapons'.format(usrnam.content)
                    c.execute(query)
                    data = c.fetchall()
                    COLUMN = 0
                    player_weapons = list([elt[COLUMN] for elt in data])
                    counter = 1
                    for shig in player_weapons:
                        time.sleep(1)
                        await ctx.author.send(str(counter) + '). ' + shig)
                        counter += 1
                    counter = 1
                    time.sleep(1)
                    msg = await bot.wait_for('message', check=check)
                    if msg and msg.content.isnumeric():
                        await ctx.author.send('wow man super')
                        battle = False

        start_rpg = False


@bot.command(name='inventory')
async def inventory(ctx):
    def check(m):
        return m.author == ctx.author

    await ctx.send('**Enter the username of the character you want inventory for: **')
    msg = await bot.wait_for('message', check=check)
    if msg:
        try:
            query = 'SELECT * FROM {}_weapons'.format(msg.content)
            c.execute(query)
            await ctx.send(c.fetchall())
            print(c.fetchall())
        except:
            await ctx.send('That is not an existing character')


keep_alive()
bot.run('ODI2NjI5NzU0NjAxNDcyMDYw.YGPQ8w.uzGjiugDdb1DXr7iJMEfYS1YDco')
