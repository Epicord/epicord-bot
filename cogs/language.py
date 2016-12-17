# NOQA
import asyncio
import requests
from discord.ext import commands


class Language:
    """Dictionaries & other word things."""

    def __init__(self, bot):
        """Cog constructor."""
        self.bot = bot

    @commands.command()
    async def define(self, word: str):
        """Retrieve a definition of the word."""
        app_id = "473851ca"
        api_key = "2b647406bfc2fde85e8a6e641b094739"

        url = "https://od-api.oxforddictionaries.com:443/api/v1/entries/en/" + word.lower()

        response = requests.get(url, headers={"app_id": app_id, "app_key": api_key})

        if response.status_code == 200:
            results = response.json()["results"][0]["lexicalEntries"][0]
            entries = results["entries"][0]["senses"][0]

            await self.bot.say("**{}**\n*{}*\n{}".format(
                word.title(),
                results["lexicalCategory"],
                entries["definitions"][0]
            ))
        else:
            await self.bot.say("No results.")

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
