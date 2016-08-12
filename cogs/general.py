import random

from discord.ext import commands
from .utils import checks


class General:
    """
    Commands that don't fit anywhere else
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["choose"], pass_context=True)
    async def choice(self, ctx, *choices: str):
        """
        Selects one of the choices passed at random
        """
        choice_list = " ".join(choices).split(";")
        choice_str = ""
        for cur in choice_list:
            choice_str += "`{}` ".format(cur)

        await self.bot.say("""{0.message.author.mention} is deciding between: {1}

I choose: {2}!""".format(
            ctx,
            choice_str,
            random.choice(choice_list)
        ))

    @commands.command(pass_context=True)
    async def eball(self, ctx, *ask: str):
        """
        Replies to question with an emoji
        """
        the_e_list = [
            ":heart_eyes_cat:",
            ":revolving_hearts:",
            ":confounded:",
            ":expressionless:",
            ":smirk_cat:",
            ":no_entry_sign:",
            ":thumbsdown:",
            ":thumbsup:",
            ":ballot_box_with_check:",
            ":cool:",
            ":sweat_drops:",
            ":fire:",
            "::ok_hand:",
            ":middle_finger:",
        ]

        quote = "`{}`".format(" ".join(ask))

        await self.bot.say("""{0.message.author.mention} {1}\n{2}""".format(
            ctx, quote, random.choice(the_e_list)
        ))


def setup(bot):
    bot.add_cog(General(bot))
