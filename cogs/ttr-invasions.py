# NOQA
import discord  # NOQA
from discord.ext import commands
import asyncio
import requests

url = 'http://www.toontownrewritten.com/api/invasions'


class TTRInv(object):
    """Check and follow cog invasions in Toontown Rewritten."""

    def __init__(self, bot):
        """Constructor."""
        self.bot = bot
        self.refresh()

    async def refresh(self):
        """Re-request the invasion info."""
        self.inv_json = requests.get(url)
        asyncio.sleep(60)
        self.refresh()

    @commands.group
    async def inv(self):
        """Receive the latest invasion info from the Toon Platoon."""
        self.inv_dict = self.inv_json.json()['invasions']
        invs = "The Toon Platoon reports that there is:\n"
        for (key, val) in self.inv_dict.items():
            if int(val['progress'].split('/')[1]) % 1000 == 0:
                summoned = "Summoned"
            else:
                summoned = "Natural"
            percent = "{0:.0%}".format(eval(val['progress']))
            inv_prop = [key, val['type'], val['progress'], percent, summoned]
            invs += (("  A **{0[1]}** invasion in **{0[0]}**:\n"
                      "    Progress: {0[3]} ({0[2]})\n"
                      "    Origin: {0[4]}\n").format(inv_prop))
        await self.bot.reply(invs)


def setup(bot):
    """Setup function."""
    bot.add_cog(TTRInv(bot))
