import json
import requests

from discord.ext import commands
from .utils import checks

from random import choice, randrange
import xml.etree.ElementTree as ET


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
                    e621_message = "{}\n<https://e621.net/post/show/{}>".format(
                            selected_post["file_url"],
                            selected_post["id"]
                        )
                await self.bot.say(e621_message)

            except IndexError:
                await self.bot.say("Sorry, no results.")


    @commands.command()
    async def gelbooru(self, *tags: str):
        """
        For all your non-furry porn needs
        """
        payload = {
            "limit": 100,
            "tags": " ".join(tags)
        }
        gelbooru = requests.get(
            "http://gelbooru.com//index.php?page=dapi&s=post&q=index",
            params=payload
        )

        root = ET.fromstring(gelbooru.text)

        try:
            selected_post = root[randrange(len(root))]

            await self.bot.say("{}\n<http://gelbooru.com/index.php?page=post&s=view&id={}>".format(
                selected_post.attrib["file_url"],
                selected_post.attrib["id"]
            ))
        except (IndexError, ValueError):
            await self.bot.say("Sorry, no results.")


def setup(bot):
    bot.add_cog(NSFW(bot))
