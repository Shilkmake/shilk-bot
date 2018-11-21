import discord
import os
from discord.ext import commands

Client = discord.Client()
client = commands.Bot(command_prefix='>')

players = {}
help_information = ">play (ahem, breathing, zvuv, lishtok, kafa, patachta, joke, mafchid, lololo," \
                   " tikanes, mishlochim, yerakot, beita_lapanim, bo_bo, oink, pokemon_go), >join, >leave"

if not discord.opus.is_loaded():
    discord.opus.load_opus("opusfile-0.9") 

    
@client.command(pass_context=True)
async def play(ctx, file_name):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    try:
        current_player = players[voice_client.session_id]
        if current_player.is_playing():
            return 0
        else:
            del players[voice_client.session_id]
    except:
        pass
    
    if voice_client:
        player = voice_client.create_ffmpeg_player("sounds/" + file_name + ".mp3")
        players[voice_client.session_id] = player
        player.start()


@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()


@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)


@client.command(pass_context=True)
async def commands(ctx):
    message = ctx.message
    await client.send_message(message.channel, help_information)

    
@client.command(pass_context=True)
async def disconnect(ctx):
    if ctx.message.author.id == os.environ.get('OWNER'):
        print(1)
        await client.close()
    

client.run(os.environ.get('TOKEN'))

