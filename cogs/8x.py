from discord.ext import commands
from .utils import checks

from random import choice, sample


class EightX:
    """
    For indecisive people all across the globe.
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['8ball'])
    async def eightball(self, *q: str):
        """
        Given a question, randomly answers it.
        """
        answers = [
            'It is certain.',
            'Don\'t count on it.',
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
        await self.bot.reply('`{}`: {}'.format(' '.join(q), choice(answers)))

    @commands.command(aliases=['8user'],
                      brief='Given a question, randomly selects a user.')
    async def eightuser(self, *q: str):
        """
        Given a question, utilizes a neural network to analyze its intent
        and intelligently selects the user that most completely fits the
        situation at hand.
        """
        user = choice(list(self.bot.get_all_members())).display_name
        await self.bot.reply('`{}`: {}'.format(' '.join(q), user))


def setup(bot):
    bot.add_cog(EightX(bot))
