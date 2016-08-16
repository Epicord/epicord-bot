# NOQA
import discord  # NOQA
from discord.ext import commands
import asyncio
import requests
from datetime import datetime

url = 'http://www.toontownrewritten.com/api/invasions'
loop = asyncio.get_event_loop()


class TTRInv:
    """Check and follow cog invasions in Toontown Rewritten."""

    def __init__(self, bot):
        """Constructor."""
        self.bot = bot
        loop.call_soon(self.refresh)

    def refresh(self):
        """Re-request the invasion info."""
        try:
            self.inv_json = requests.get(url)
            time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
            print("Invasions refreshed:", time)
        except Exception as e:
            error_msg = "Encountered {0} while attempting to refresh."
            print(error_msg.format(type(e).__name__))

        # await asyncio.sleep(60)
        if self.bot.get_cog('TTRInv') is not None:
            loop.call_later(15, self.refresh)

    @commands.command()
    async def inv(self):
        """Receive the latest invasion info from the Toon Platoon."""
        self.inv_dict = self.inv_json.json()['invasions']
        invs = "The Toon Platoon has reported these invasions:\n"
        for (key, val) in self.inv_dict.items():
            if int(val['progress'].split('/')[1]) % 1000 == 0:
                summoned = "Summoned"
            else:
                summoned = "Natural"
            percent = "{0:.0%}".format(eval(val['progress']))
            inv_prop = [key, val['type'], val['progress'], percent, summoned]
            invs += (("  **{0[1]}** invasion in *{0[0]}*:\n"
                      "    Progress: {0[3]} ({0[2]})\n"
                      "    Origin: {0[4]}\n").format(inv_prop))
        await self.bot.say(invs)


def setup(bot):
    """Setup function."""
    bot.add_cog(TTRInv(bot))
