# bot.py
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #List of standard response
    welcome_quotes = [
        'Hey welcome to the server',
        'Hi there!'
    ]

    if message.content == 'Hi': #Checking the message content, ex : !help -> to print all the commands this bot can help with
        response = random.choice(welcome_quotes) 
        await message.channel.send(response)   #sending response
client.run(TOKEN)
