import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "+")

chat_filter = ["+MINECRAFT", "+SPECIAL",]
bypass_list = []

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="with Alts! | v0.1 | +help"))
    print("De bot is klaar voor gebruik!")
    
@client.event
async def on_message(message):
    if message.content == "+minecraft":
        await client.send_message(message.author, random.choice([" **Alt Generator** \n Here is your Minecraft Alt! \n sander.eulderink12345678910@gmail.com:MVV29Hera \n \n Made by BlockBuster594✓ᵛᵉʳᶦᶠᶦᵉᵈ#6784 ", " **Alt Generator** \n Here is your Minecraft Alt! \n Salmanuk00@gmail.com:Salman12 \n \n Made by BlockBuster594✓ᵛᵉʳᶦᶠᶦᵉᵈ#6784 "" **Alt Generator** \n Here is your Minecraft Alt! \n Grimezo123@gmail.com:Liveair123 \n \n Made by BlockBuster594✓ᵛᵉʳᶦᶠᶦᵉᵈ#6784 "," **Alt Generator** \n Here is your Minecraft Alt! \n supersidge@hotmail.co.uk:Mlgrock5! \n \n Made by BlockBuster594✓ᵛᵉʳᶦᶠᶦᵉᵈ#6784 ", " **Alt Generator** \n Here is your Minecraft Alt! \n kayleegun9@gmail.com:maggie2011 \n \n Made by BlockBuster594✓ᵛᵉʳᶦᶠᶦᵉᵈ#6784 ", " **Alt Generator** \n Here is your Minecraft Alt! \n taikaviitta72@gmail.com:Hassu2013 \n \n Made by BlockBuster594✓ᵛᵉʳᶦᶠᶦᵉᵈ#6784 ", " **Alt Generator** \n Here is your Minecraft Alt! \n tigarman@charter.net:Bullspit1 \n \n Made by BlockBuster594✓ᵛᵉʳᶦᶠᶦᵉᵈ#6784 ", " **Alt Generator** \n Here is your Minecraft Alt! \n bentoncox97@hotmail.com:Benton3397 \n \n Made by BlockBuster594✓ᵛᵉʳᶦᶠᶦᵉᵈ#6784 ", " **Alt Generator** \n Here is your Minecraft Alt! \n willtskywalker@hotmail.com:star1997wars \n \n Made by BlockBuster594✓ᵛᵉʳᶦᶠᶦᵉᵈ#6784 ", " **Alt Generator** \n Here is your Minecraft Alt! \n patrickcoleman1@gmail.com:Darkcop123! \n \n Made by BlockBuster594✓ᵛᵉʳᶦᶠᶦᵉᵈ#6784 ", " **Alt Generator** \n Here is your Minecraft Alt! \n alice_1996@hotmail.co.uk:Crystal7 \n \n Made by BlockBuster594✓ᵛᵉʳᶦᶠᶦᵉᵈ#6784 ", " **Alt Generator** \n Here is your Minecraft Alt! \n zombatron@gmail.com:Marley9002 \n \n Made by BlockBuster594✓ᵛᵉʳᶦᶠᶦᵉᵈ#6784 ", " **Alt Generator** \n Here is your Minecraft Alt! \n kaidewolff@gmail.com:NJ00789932 \n \n Made by BlockBuster594✓ᵛᵉʳᶦᶠᶦᵉᵈ#6784 ", " **Alt Generator** \n Here is your Minecraft Alt! \n cvichyde@googlemail.com:Charlie50 \n \n Made by BlockBuster594✓ᵛᵉʳᶦᶠᶦᵉᵈ#6784 ", " **Alt Generator** \n Here is your Minecraft Alt! \n jnminardi@optonline.net:Cheech27 \n \n Made by BlockBuster594✓ᵛᵉʳᶦᶠᶦᵉᵈ#6784 ",]))
    if message.content == "+special":
        await client.send_message(message.author, random.choice([" **Alt Generator** \n Here is your Special Alt! \n email:pass \n \n Made by BlockBuster594✓ᵛᵉʳᶦᶠᶦᵉᵈ#6784 ", " **Alt Generator** \n Here is your Special Alt! \n email:pass \n \n Made by BlockBuster594✓ᵛᵉʳᶦᶠᶦᵉᵈ#6784 "]))
    if message.content == "+help":
        await client.send_message(message.channel, "**Commands** \n \n**+help** \n Show this. \n \n**+minecraft** \n Only works in the generator channel. \n \n**+special** \n Only works in the generator channel. \n \n**+shop** \n Sends the shop link.")
    if message.content == "+shop":
        await client.send_message(message.channel, "**Shop:** \nhttps://selly.gg/@Refresh")
    contents = message.content.split(" ") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            await client.delete_message(message)
        
client.run("NTA5Nzk2NzI1MDc1MjE0Mzcz.DsTNlg.CsA0NN2q7ZW4sZySAL636JgeZ2Q")
