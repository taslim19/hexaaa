from telethon import events , TelegramClient
from asyncio import sleep as zzz
from random import randint
from re import match

#dont edit else gay this constant
api_id = 2282111
api_hash = 'da58a1841a16c352a2a999171bbabcad'
bot = TelegramClient('session' , api_id , api_hash)
chat = 572621020

#edit the list
list = ["Charizard", "Blastoise",  "Alakazam", "Gengar", "Kangaskhan", "Pinsir", "Gyarados", "Aerodactyl", "Mewtwo", "Houndoom", "Sceptile", "Gardevoir", "Salamence", "Metagross", "Latias", "Latios", "Rayquaza", "Lopunny", "Lucario", "Gallade", "Wimpod", "Greninja", "Froakie", "Hawlucha", "Frillish", "Arrokuda", "Darmanitan", "Primarina", "Popplio", "Floette", "Florges", "Dreepy", "Sneasler", "Starly", "Espeon", "Jolteon", "Mudkip", "Squirtle", "Rotom", "Drakloak", "Inteleon"]
@bot.on(events.NewMessage(outgoing=True,pattern='/go'))
async def begin(event):
    global hunt
    hunt = True
    x = await bot.send_message(chat , "/hunt")
    try:  
     async with bot.conversation('@Hexamonbot') as conv:
       await conv.get_response(x.id)
    except:
       await zzz(3,5)
       await bot.send_message(chat , "/hunt")
    for i in range(5,10000):
      await zzz(randint(5000, 6020))
      await bot.send_message(chat , "/hunt")

@bot.on(events.NewMessage(chats=chat,incoming=True))
async def hunt(event):
    if hunt == True:
     text = event.message.text
     hun = True
     message = await bot.get_messages(chat, ids=event.message.id)
     if ("Shiny" in text):
        bot.disconnect()
     elif("TM" in text):
        print(event.message.text)
        await zzz(randint(3,5))
        x = await bot.send_message(chat , "/hunt")
        try:  
         async with bot.conversation('@Hexamonbot') as conv:
           await conv.get_response(x.id)
        except:
           await zzz(5,6)
           await bot.send_message(chat , "/hunt")
     elif any(item in text for item in list):
        await message.click(text="Battle")
        await message.click(text="Battle")
        await message.click(text="Battle")
     elif("A wild" in text or "An expert" in text):
      if hun == False:
       pass
      else:
       await zzz(randint(3,5))
       x = await bot.send_message(chat , "/hunt")
       try:  
        async with bot.conversation('@Hexamonbot') as conv:
          await conv.get_response(x.id)
       except:
          await zzz(3,5)
          await bot.send_message(chat , "/hunt")
      

@bot.on(events.NewMessage(chats=chat,incoming=True))
async def hunt(event):
   print(event.message.text)
   if event.message.text[:13] == "Battle begins":
        message = await bot.get_messages(chat, ids=event.message.id)
        await zzz(21)
        await message.click(text = "Poke Balls")
        await message.click(text = "Poke Balls")
        await message.click(text = "Poke Balls")      


@bot.on(events.MessageEdited(chats=chat))
async def cacther(event):
   message = await bot.get_messages(chat, ids=event.message.id)
   await message.click(text = "Poke Balls")
   await message.click(text = "Poke Balls")
   await message.click(text = "Poke Balls") 
   if event.message.text[:4] == "Wild":
      await zzz(1)
      await message.click(text = "Regular")
      await message.click(text = "Regular")
      await message.click(text = "Regular")
   if any(keyword in event.message.text for keyword in ['fled', 'fainted', 'caught']):
      await zzz(randint(3,5))
      x = await bot.send_message(chat , "/hunt")
      try:  
       async with bot.conversation('@Hexamonbot') as conv:
         await conv.get_response(x.id)
      except:
         await zzz(3,5)
         await bot.send_message(chat , "/hunt")



@bot.on(events.NewMessage(outgoing=True,pattern='/stop'))
async def stop(event):
    global hunt
    hunt = False


bot.start()
bot.run_until_disconnected()
