import discord
import os 
# import requests
# import json 
import random
from replit import db

intents = discord.Intents.default()
client = discord.Client(intents=intents)

words = ["noob", "nub", "Noob", "Nub", "NOOB", "NUB"]

sent_words = [
  "Did you just say noob!! You noob",
             "Yo Noobs",
             "Noob Only",
             "Could you be more noob!"]

# def get_quote():
#     response = requests.get("https://zenquotes.io/api/random")
#     json_data = json.loads(response.text)
#     quote = json_data[0]['q']  + " -" + json_data[0]['a']
#     return(quote)

def update_words(words_message):
  if "noobs" in db.keys():
    words = db["noobs"]
    words.append(words_message)
    db["noobs"] = words
  else:
    db["noobs"] = [words_message]


def delete_words(index):
  words = db["noobs"]
  if len(words) > index:
    del words[index]
    db["noobs"] = words

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
  
    # if msg.startswith('$noob'):
    #     quote = get_quote()
    #     await message.channel.send(quote)

    options = sent_words
    if "noobs" in db.keys():
      options = options + db["noobs"]
  
    if any(word in msg for word in words):
        await message.channel.send(random.choice(options))

    if msg.startswith("$new"):
      words_message = msg.split("$new",1)[1]
      update_words(words_message)
      await message.channel.send

client.run(os.getenv('TOKEN'))
