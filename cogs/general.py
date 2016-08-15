import random

from discord.ext import commands
from .utils import checks


class General:
    """
    Commands that don't fit anywhere else
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["choose"])
    async def choice(self, *choices: str):
        """
        Selects one of the choices passed at random
        """
        choice_list = " ".join(choices).split(";")
        choice_str = ""
        for cur in choice_list:
            choice_str += "`{}` ".format(cur)

        await self.bot.reply("""is deciding between: {}

I choose: {}!""".format(choice_str, random.choice(choice_list)))

    @commands.command()
    async def eball(self, *ask: str):
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
            ":ok_hand:",
            ":middle_finger:",
        ]

        quote = "`{}`".format(" ".join(ask))

        await self.bot.reply("""{}\n{}""".format(
            quote, random.choice(the_e_list)
        ))

    @commands.command(name='8ball')
    async def eightball(self, *q: str):
        """
        Given a question, randomly answers it.
        """
        answers = [
            'It is certain.',
            'Of course.',
            ':crystal_ball: Perhaps...',
            'That\'s not a good idea.',
            'You\'ll just have to wait and see.',
            'Outlook good.',
            'Yes.',
            'No.',
            'Most likely ( ͡° ͜ʖ ͡°)',
            'Yes, definitely! (๑✧◡✧๑)',
            'Don\'t count on it (っ◞‸◟c)',
            'Not so sure... probably not.',
            'Not sure, but likely yes. :^)',
            'Without a doubt (^～^)',
            'That\'s completely absurd.',
            'No, absolutely not! :thumbsdown:',
            'I don\'t know m8 ʅ(◔౪◔ ) ʃ',
            ':crystal_ball: The answer is not what you think.'
        ]
        await self.bot.reply('`{}`: {}'.format(' '.join(q),
                                               random.choice(answers)))

    @commands.command(name='8user',
                      brief='Given a question, randomly selects a user.')
    async def eightuser(self, *q: str):
        """
        Given a question, utilizes a neural network to analyze its intent
        and intelligently selects the user that most completely fits the
        situation at hand.
        """
        user = random.choice(list(self.bot.get_all_members())).display_name
        await self.bot.reply('`{}`: {}'.format(' '.join(q), user))


def setup(bot):
    bot.add_cog(General(bot))
