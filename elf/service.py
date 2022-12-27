import discord
from logging import info, warning, basicConfig, INFO
from discord.ext import commands
from discord.ext.commands.context import Context
from elf_dict import *

basicConfig(level=INFO)

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)
@client.event
async def on_ready():
    warning(f'currently login as {client.user}')

@client.event
async def on_message(message:discord.message.Message):
    # mute itself
    if message.author == client.user:
        return
    if not message.guild:
        warning(f"recv: {message.content}")
        if message.content[0] == "!":
            await client.process_commands(message)
        else:
            await message.channel.send(query(message.content))
    else:
        if message.channel.id == 1056954463862132736:
            await message.channel.send("only accept private message >_<")
    
@commands.command('export', help="export the current save of dictionary")
async def _export(ctx:Context):
    await ctx.send(export_dict())

@commands.command('import', help="import the current save of dictionary")
async def _import(ctx:Context, save:str):
    '''
    use multiprocessing to prevent request stuck bot during importing
    '''
    import multiprocessing
    proc = multiprocessing.Process(target=load_dict, args=(save, ))
    proc.start()
    proc.join(5)
    if not proc.is_alive():
        await ctx.send("import save success :D")
    else:
        proc.kill()
        await ctx.send("import failed :(")

@commands.command('reset', help="reset the dictory to original state")
async def _reset(ctx:Context):
    reset()
    await ctx.send("reset success 的啦")

client.add_command(_export)
client.add_command(_import)
client.add_command(_reset)

# please do not use it to echo any message, tkx
client.run('MTA1MzIyMzM3NDY2MDMxMzEwOA.GHF6E3.9PXIxl1I0DNPvdUv6wuBz3EOhdHkdh5sCQeZP0')