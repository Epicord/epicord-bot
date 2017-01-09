# NOQA
import asyncio
import requests
from xml.etree import ElementTree
from itertools import islice
from discord.ext import commands


class Language:
    """Dictionaries & other word things."""

    def __init__(self, bot):
        """Cog constructor."""
        self.bot = bot

    @commands.command()
    async def define(self, word: str):
        """Retrieve a definition of the word."""
        api_key = "e02fb0b8-5f3e-4d5c-b868-87dd7de88974"

        # Checks for mutliple words and only uses first
        if " " in word:
            word = word.split(" ")[0]

        url = "http://www.dictionaryapi.com/api/v1/references/collegiate/xml/{}?key={}".format(word.lower(), api_key)

        response = requests.get(url)
        results = ElementTree.fromstring(response.text)

        for entry in islice(results, 0, 3):
            if entry.tag == "suggestion":
                await self.bot.say("That's not a word")
                break
            word = entry.find("ew").text
            word_type = entry.find("fl").text
            word_def = entry.find("def").find("dt").text

            try:
                if word_def == ":":
                    word_def = entry.find("def").findall("dt")[1].text

                await self.bot.say("**{}**\n*{}*\n{}".format(
                    word, word_type, word_def)
                )
            except IndexError:
                continue


    @commands.command()
    async def syn(self, word: str):
        """Get a list of 5 synonyms for the requested word."""
        api_key = "ce01609f490e4f8c5b5ab55ce80d9530"

        url = "http://words.bighugelabs.com/api/2/{}/{}/json".format(
            api_key,
            word.lower()
        )

        response = requests.get(url)

        if response.status_code == 200:
            # Get list of keys
            syn_keys = list(response.json().keys())
            # Start response
            syn_string = "**{}**\n".format(word.title())

            # Add synonyms to string
            for key in syn_keys:
                # Get first 5 synonyms
                syn_list = ", ".join(response.json()[key]["syn"][:5])

                syn_string += "*{}*\n{}\n".format(key, syn_list)

            await self.bot.say(syn_string)
        else:
            await self.bot.say("No results.")


def setup(bot):
    """Setup function."""
    bot.add_cog(Language(bot))
