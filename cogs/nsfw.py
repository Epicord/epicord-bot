import json
import requests
from discord.ext import commands
from random import choice
from .utils import checks


class NSFW:
    """
    All the porn \o/
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def e621(self, *tags: str):
        """
        Retrieves a post based on tags and returns a random image from e621
        """
        if len(tags) > 6:
            await self.bot.say("Sorry, e621 has a 6 tag maximum.")
        else:
            payload = {
                "tags": " ".join(tags),
                "limit": 320
            }
            e621_response = requests.get(
                "https://e621.net/post/index.json",
                params=payload
            )
            posts = json.loads(e621_response.text)
            try:
                selected_post = choice(posts)

                if selected_post["file_ext"] in ["swf", "webm"]:
                    e621_message = "https://e621.net/post/show/{}".format(
                        selected_post["id"]
                    )
                else:
                    e621_message = "{}\nhttps://e621.net/post/show/{}".format(
                            selected_post["file_url"],
                            selected_post["id"]
                        )
                await self.bot.say(e621_message)

            except IndexError:
                await self.bot.say("Sorry, no results.")


def setup(bot):
    bot.add_cog(NSFW(bot))
