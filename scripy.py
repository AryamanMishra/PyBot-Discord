# heroku deployed

import discord as DS
import random
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv('.env')

client = DS.Client()

links_motivation = ['https://www.youtube.com/watch?v=g-jwWYX7Jlo','https://www.youtube.com/watch?v=mgmVOuLgFB0','https://www.youtube.com/watch?v=V2EfL1j4KYE','https://www.youtube.com/watch?v=u_ktRTWMX3M','https://www.youtube.com/watch?v=yJYiOzTAZ-o']


links_games = ['https://www.youtube.com/watch?v=BH4GQyqq3gI','https://www.youtube.com/watch?v=TlchFP6pNEU','https://www.youtube.com/watch?v=lDKnapyjLjA','https://www.youtube.com/watch?v=SDra2IVDV9E','https://www.youtube.com/watch?v=mCds5B2SHCM','https://www.youtube.com/watch?v=lozvzBhwxZI','https://www.youtube.com/watch?v=YsUFfK-bDhg']

links_bb = ['https://www.youtube.com/watch?v=h25S27rh4oY','https://www.youtube.com/watch?v=dFKhWe2bBkM&t','https://www.youtube.com/watch?v=F1qFB4n9K6Q','https://www.youtube.com/watch?v=jzbMxWvnlGw','https://www.youtube.com/watch?v=OIr31AZtVSk','https://www.youtube.com/watch?v=53FPC7tqbNI','https://www.youtube.com/watch?v=fMK6n3JqfMw']

oe = []
for i in (1,100):
    oe.append(i)

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + str(json_data[0]['a'])
    return quote

@client.event
async def on_ready():
    print('Hey I have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!motivate'):
        quote = get_quote()
        await message.channel.send(quote)
    if message.content.startswith('!support'):
        await message.channel.send('Your best support comes from inside')
    if message.content.startswith('!video'):
        await message.channel.send('Follow this link for the best motivational video: ' + random.choice(links_motivation))
    if message.content.startswith('!games'):
        await message.channel.send('Follow this link for the best gaming video: ' + random.choice(links_games))
    if message.content.startswith('!manual'):
        await message.channel.send('Hello there I am PyBot ' + 
        'I will try to give you the best motivation along side fun gaming and motivational videos. ' + '\n' 
        
        'Thanks for the support!! ' + '\n' + 'Use !motivate for motivation quotes '+ '\n' + 'Use !support for supporting quotes ' + '\n' 'Use !video for motivating videos' + '\n' + 'Use !games for gaming videos' + '\n'  + 'Use !manual for manual')

        
client.run(os.getenv('TOKEN'))
