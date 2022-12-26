'''from pytube import YouTube

yt = YouTube(input("What is the link of your YouTube video?"))

print(f"Downloading {yt.title}!")

stream = yt.streams.filter(only_audio = True).first()
stream.download()'''

'''------------------------------------------------------------------------------------------------'''
import asyncio
import os
from discord.ext import commands
import discord
from dotenv import load_dotenv
from pytube import YouTube

client = commands.Bot(command_prefix = '!', intents = discord.Intents.all())

@client.event
async def on_ready():
    print(f"Logged in as {client.user} with ID: {client.user.id}!")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency)*1000}ms")

@client.command()
async def play(ctx, url):
    async def play1(ctx, url):
        yt = YouTube(url)
        print(f"Downloading {yt.title}")
        stream = yt.streams.filter(only_audio=True).first()
        destination = "C:\\Users\\nikla\\Projects\\ARC\ARC_Bot\\YouTube"
        out_file = stream.download(output_path=destination)
        # base, ext = os.path.splitext(out_file)
        new_file = 'C:\\Users\\nikla\\Projects\ARC\\ARC_Bot\\YouTube\\song.mp3'
        os.rename(out_file, new_file)
        
        
        print(f"{yt.title} has been seccessfully doanloaded.")
        await ctx.send('Downloaded!')  ## DEBUG
        await ctx.send(f"Started playing {yt.title}.")
        ffmpeg_location = "C:\\Users\\nikla\Projects\\ARC\\ARC_Bot\\ffmpeg-N-109433-g48d5aecfc4-win64-gpl\\bin\\ffmpeg.exe"
        vc.play(discord.FFmpegPCMAudio(executable=ffmpeg_location, source=new_file))
        elapsed_time = 0
        while elapsed_time <= yt.length + 1:
            elapsed_time += 1
            await asyncio.sleep(1)
        os.remove(new_file)
        await vc.disconnect() 
        await ctx.send("The bot has left the voice channel.")
    
    if ctx.author.voice:
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        if voice == None:
            await ctx.send("Connecting to your voice channel...")
            channel = ctx.author.voice.channel
            vc = await channel.connect()
            #await vc.connect()
            await ctx.send("Connected to your voice channel.")
            await play1(ctx, url)
        else:
            await play1(ctx, url)
    else:
        await ctx.send("You need to be in a voice channel first.")
        # COULD MOVE USER INTO A VC AND MOVE ON
    

load_dotenv()
client.run(os.getenv('TOKEN'))