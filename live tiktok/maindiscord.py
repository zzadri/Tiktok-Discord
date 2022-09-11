from re import L
from time import sleep
import discord
import random
import pygame
from discord.ext import commands

pygame.mixer.init()
pygame.mixer.music.load("levelxp-sounds-minecraft-sound-effects-for-editing.mp3")


colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1, 0x124242]

i = 0

l = 0
f = 0
d = 0

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = "!*", intents=intents)

@bot.event
async def on_ready():
    while True:
        sleep(2)
        with open("chat.txt", "r+", encoding="utf-8") as file:
            chat = file.readline()
            if chat[0:3] == "[0]":

                chat2 = chat[4:10000]
                
                chated = discord.Embed(title=f"**Merci pour ton commentaire !**", description= chat2, color=random.choice(colors))
                await bot.get_channel(957310101138575460).send(embed = chated)

                fic1 = open("chat.txt", "w", encoding="utf-8")
                txt = chat.replace('[0] ', '[1] ')
                fic1.write(f"{txt}")

                

        with open("like.txt", "r+", encoding="utf-8") as file:
            like = file.readline()
            if like[0:3] == "[0]":

                like2 = like[4:1000]
                
                liked = discord.Embed(title=f"**Merci d'avoir like -> {like2}**", color=random.choice(colors))
                await bot.get_channel(957310101138575460).send(embed = liked)

                fic2 = open("like.txt", "w", encoding="utf-8")
                txt2 = like.replace('[0] ', '[1] ')
                fic2.write(f"{txt2}")
                


        with open("join.txt", "r+", encoding="utf-8") as file:
            join = file.readline()
            if join[0:3] == "[0]":

                join2 = join[4:1000]

                joined = discord.Embed(title=f"**Merci d'être la -> {join2}**", color=random.choice(colors))
                await bot.get_channel(957310101138575460).send(embed = joined)

                fic3 = open("join.txt", "w", encoding="utf-8")
                txt3 = join.replace('[0] ', '[1] ')
                fic3.write(f"{txt3}")





        with open("giftr.txt", "r+", encoding="utf-8") as file:
            gift = file.readline()
            if gift[0:3] == "[0]":

                gift2 = gift[4:1000]

                gifted = discord.Embed(title=f"***Merci à -> {gift2}***", color=random.choice(colors), url="https://discord.gg/8hvJgtg8Bj")
                gifted.set_thumbnail(url="https://us.123rf.com/450wm/koblizeek/koblizeek2003/koblizeek200300140/142843433-conception-d-ic%C3%B4ne-de-bo%C3%AEte-cadeau-symbole-pr%C3%A9sent-de-vecteur-isol%C3%A9-sur-fond-blanc-.jpg?ver=6")
                #don = bot.get_channel(957310101138575460)
                #await don.edit(name=f"dernier donateur: {gift2}")
                await bot.get_channel(957310101138575460).send("ㅤ \n ㅤ \n ㅤ\nㅤ")
                pygame.mixer.music.play()
                await bot.get_channel(957310101138575460).send(embed = gifted)
                await bot.get_channel(957310101138575460).send("ㅤ \n ㅤ \n ㅤ\nㅤ")
                
                


                fic4 = open("giftr.txt", "w", encoding="utf-8")
                txt4 = gift.replace('[0] ', '[1] ')
                fic4.write(f"{txt4}")

        with open("follow.txt", "r+", encoding="utf-8") as file:
            follow = file.readline()
            if follow[0:3] == "[0]":

                follow2 = follow[4:1000]

                follower = discord.Embed(title=f"**Merci de t'être abbonée -> {follow2}**", color=random.choice(colors))
                await bot.get_channel(957310101138575460).send(embed = follower)

                fic5 = open("follow.txt", "w", encoding="utf-8")
                txt5 = follow.replace('[0] ', '[1] ')
                fic5.write(f"{txt5}")
         
  


bot.run('token')
