# NOQA
import asyncio
import json
import os
import discord  # NOQA
from discord.ext import commands
from cogs.utils import checks


bot = commands.Bot(command_prefix='~', description='''
                   EpicordBot - created in the advent of BooBot's demise.
                   ''', pm_help=None, help_attrs=dict(hidden=True))
exts = ['cogs.nsfw']


@bot.event
async def on_ready():
    """Print ready messages."""
    print('Logged in {}#{} id:{}'.format(bot.user.name, bot.user.discriminator,
                                         bot.user.id))
    for extension in exts:
        try:
            bot.load_extension(extension)
            print('{} loaded'.format(extension))
        except Exception as e:
            print('{} failed to load :c\n{}: {}'.format(extension,
                                                        type(e).__name__, e))


@bot.event
async def on_message(m):
    """Event called when a message is received."""
    await bot.process_commands(m)


@bot.command(hidden=True)
@checks.is_owner()
async def load(*, module: str):
    """Load a cog."""
    module = module.strip()
    try:
        bot.load_extension(module)
    except Exception as e:
        await bot.say('Ouch.\n{}: {}'.format(type(e).__name__, e))
    else:
        await bot.say('Got it, {} loaded.'.format(module))


@bot.command(hidden=True)
@checks.is_owner()
async def unload(*, module: str):
    """Unload a cog."""
    module = module.strip()
    try:
        bot.unload_extension(module)
    except Exception as e:
        await bot.say('Ouch.\n{}: {}'.format(type(e).__name__, e))
    else:
        await bot.say('Alright, {} unloaded.'.format(module))


@bot.command(hidden=True)
@checks.is_owner()
async def reload(*, module: str):
    """Reload a cog."""
    module = module.strip()
    try:
        bot.unload_extension(module)
        await asyncio.sleep(3)
        bot.load_extension(module)
    except Exception as e:
        await bot.say('Ouch.\n{}: {}'.format(type(e).__name__, e))
    else:
        await bot.say('Okay, {} reloaded.'.format(module))

try:
    token = json.load(open('config.json'))["token"]
# for travis-ci
except FileNotFoundError as e:
    token = os.environ['TOKEN']
finally:
    bot.run(token)
