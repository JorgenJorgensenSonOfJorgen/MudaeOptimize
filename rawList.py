#compile an updated bundle spreadsheet from mudae bot

import discord
import re
import asyncio
client = discord.Client(self_bot = True)

f= open("info.txt", encoding = 'utf8')
bundles = f.read().splitlines()
f.close()
updated = open("updated.txt", "w") 
updated.write('')
updated.close()
updated = open("updated.txt", "a", encoding = 'utf8') #we want to clear the file each time

index = 0

for i in range(len(bundles)):

    bundles[i] = bundles[i].split('\t')[0] #we only want the name

@client.event
async def on_ready():
    print("ready!")

@client.event
async def on_message(message):

    global index

    if message.content == '-s':
            
        await message.channel.send('$imat {}'.format(bundles[0])) #request the bundle info of first bundle
        updated.write(bundles[0])

    elif message.author.id == 432610292342587392: #message from mudae bot

        index += 1 
        emb = message.embeds[0]
        tot = re.search('/\d+',emb.author.name).group()
        tot = (tot[1:len(tot)]) 

        wife = emb.description      
        wife = re.search('\d+ \$wa',wife).group()
        wife = (wife[0:len(wife)-4])

        #write this info on the appropriate line

        updated.write('\t{}\t{}'.format(tot,wife))

        if index < len(bundles): #call the next bundle if this was not the last one.

            #write the new bundle name along with new line - this might need a delay or we could have a checker to see if it stalls (say, waits 5 seconds and if nothing shows up, then we try the command again): We implemented both LOL
            
            await asyncio.sleep(0.5)
            updated.write('\n{}'.format(bundles[index]))
            await message.channel.send('$imat {}'.format(bundles[index]))
            indexInitial = index
            await asyncio.sleep(8.5) #this builds up and is very taxing. Causes program to go through periods of 8 second delays

            if indexInitial == index: #if after 8.5 seconds the index still hasn't changed, redo the command.

                await message.channel.send('$imat {}'.format(bundles[index]))

        else:

            updated.close()

client.run('OTYyODQxMjU1NTQzNDU1ODM0.YlNZ8g.Z15hdXEpeTnvJpAUvt9hNeB9xN0')

