import discord
from discord.ext import commands
import random
import string
import os

color=0x00ffe6
token = "MTE5MjkxNTUzMDg0NDIxMzM4OA.G0UP2B.7h9SZdYjXYWxzh_ZlTgT3gWP4UdjYbUBORvu54"
client = commands.Bot(command_prefix=".", intents=discord.Intents.all(), help_command=None)
owner = [1182014680735166597]

@client.event
async def on_ready():
    print("online")

@client.command()
async def help(ctx):
    embed = discord.Embed(title = "HELP", description = "check [code]\ngen\nsecret", color=color)
    await ctx.reply(embed=embed)

@client.command()
async def secret(ctx):
    embed = discord.Embed(title="Admin Commands", description="resetbackend\nadd\nshowfreeauth\nresetfree\nshowpaidauth", color=color)
    await ctx.reply(embed=embed)

@client.command()
async def resetbackend(ctx):
    if ctx.author.id in owner:
        await ctx.reply("> [:exclamation:] RESETTING ALL THE DATABASES AND REFRESHING THE BACKEND.")
        os.remove("auth\\auth.txt")
        os.remove("auth\\premium_auth.txt")
        file = open("auth\\auth.txt","w")
        file2 = open("auth\\premium_auth.txt","w")
        file.close()
        file2.close()
        await ctx.reply("> Backend has been reset, Thank you for chosing Koala's Wizzhut <3")
    else:
        await ctx.reply("command ignored.")

@client.command()
async def check(ctx, *,auth):
    file = open("auth\\auth.txt","r")
    freeauth = file.read().split()
    file2 = open("auth\\premium_auth.txt","r")
    premauth = file2.read().split()
    if auth in freeauth or auth in premauth:
        embed = discord.Embed(title="auth", description="Valid",color=color)
        await ctx.reply(embed=embed)
    else:
        embed = discord.Embed(title="auth", description="Invalid", color=color)
        await ctx.reply(embed=embed)

@client.command()
async def gen(ctx):
    code = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=7))
    file = open("auth\\auth.txt","a")
    written = file.write(f" {code}")
    file.close()
    embed = discord.Embed(title="Generated Code", description=code, color=color)
    await ctx.author.send(embed = embed)

@client.command()
async def add(ctx,*,auth):
    if ctx.author.id in owner:
        file = open("auth\\premium_auth.txt","a")
        file.write(f" {auth}")
        file.close()
        await ctx.reply(f"> Added auth {auth}")
    else:
        await ctx.reply("command ignored.")

@client.command()
async def showfreeauth(ctx):
    if ctx.author.id in owner:
        file = open("auth\\auth.txt", "r")
        reader = file.readlines()
        await ctx.reply(reader)
    else:
        await ctx.reply("command ignored.")

@client.command()
async def resetfree(ctx):
    if ctx.author.id in owner:
        file = open("auth\\auth.txt", "w")
        file.write("")
        file.close()
        await ctx.reply("> Reset all auth keys for free tier.")
    else:
        await ctx.reply("command ignored.")

@client.command()
async def showpaidauth(ctx):
    if ctx.author.id in owner:
        file = open("auth\\premium_auth.txt","r")
        reader = file.readlines()
        await ctx.reply(reader)
    else:
        await ctx.reply("command ignored.")

client.run(token)