import discord
import os
import requests
import json

#current commands (prefix $): greeting, fact, quote, cat
client = discord.Client()

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
    
  if message.content.startswith('$greeting'):
    await message.channel.send("Hello!")

  if message.content.startswith('$fact'):
    fact = get_fact()
    await message.channel.send(fact)
    
  if message.content.startswith('$quote'):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content.startswith('$cat'):
    cat = get_cat()
    await message.channel.send(cat)

client.run(os.getenv('TOKEN'))