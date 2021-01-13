import discord
import os
import requests
import json
import random

client = discord.Client()

sykkuno = [
"Um...",
"Ehh",
"I’m a streamer for fun.",
"I’m a small streamer for fun.",
"I just got lucky.",
"Girls just aren't into me like that.",
"Good enough for me.",
"l'm just over for dinner.",
"Mornin' Rae! (Everytime Valkyrae goes online in the morning)",
"I just got new lights.",
"The uber bill is getting expensive.",
"I need to pay my water bill, guys.",
"That's more than I make in a week.",
"I'm charging in like a maniac!",
"*covers his mouth with his hand everytime he laughs*",
"Hi Corpse!",
"I told him i would protect him!",
"I can't kill him! (Corpse)",
"I'm the biggest Toast simp",
"Oh Jesus! ... ",
"You guys actually killed him ?! You're crazy!",
"It definitely could've been me",
"Arf arf!",
"Babushka, Babushka!",
"That's crazy"
]

def get_fact():
  response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
  json_data = json.loads(response.text)
  fact = json_data['text']
  return (fact)

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def get_cat():
  response = requests.get('https://api.thecatapi.com/v1/images/search')
  json_data = json.loads(response.text)
  cat = json_data[0]['url']
  return(cat)

@client.event
async def on_ready():
  print('Bot online as {0.user}'.format(client))

@client.event
async def on_message(message):

  if message.author == client.user:
    return
    
  msg = message.content

  if msg.startswith('$greeting'):
    await message.channel.send("Hello!")

  if msg.startswith('$fact'):
    fact = get_fact()
    await message.channel.send(fact)
    
  if msg.startswith('$quote'):
    quote = get_quote()
    await message.channel.send(quote)

  if msg.startswith('$cat'):
    cat = get_cat()
    await message.channel.send(cat)
  
  if msg.startswith('$sykkuno'):
    await message.channel.send(random.choice(sykkuno))

client.run(os.getenv('TOKEN'))