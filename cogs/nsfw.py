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

    @commands.command(pass_context=True)
    async def e621(self, ctx, *tags: str):
        """
        All the best furry porn! (and best porn in general obvsly)
        """
        if ctx.message.channel.id in json.load(open('config.json'))["r18"]:
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
                        e621_message = """Found `{}` results for `{}` tags
    {}
    <https://e621.net/post/show/{}>""".format(
                                len(posts),
                                len(tags),
                                selected_post["file_url"],
                                selected_post["id"]
                            )
                    await self.bot.say(e621_message)

                except IndexError:
                    await self.bot.say("Sorry, no results.")

    @commands.command(pass_context=True, aliases=["gel"])
    async def gelbooru(self, ctx, *tags: str):
        """
        For all your non-furry porn needs

        Use 'no-preview' to disable image previews
        """
        if ctx.message.channel.id in json.load(open('config.json'))["r18"]:
            tags = " ".join(tags).split(" ")
            no_preview = False
            if "no-preview" in tags:
                tags.remove("no-preview")
                no_preview = True
            payload = {
                "limit": 100,
                "tags": tags
            }
            gelbooru = requests.get(
                "http://gelbooru.com//index.php?page=dapi&s=post&q=index",
                params=payload
            )

            root = ET.fromstring(gelbooru.text)

            try:
                selected_post = root[randrange(len(root))]
                if no_preview:
                    direct_url = "<{}>".format(selected_post.attrib["file_url"])
                else:
                    direct_url = "{}".format(selected_post.attrib["file_url"])

                await self.bot.say("""http:{}
    <http://gelbooru.com/index.php?page=post&s=view&id={}>""".format(
                    direct_url,
                    selected_post.attrib["id"]
                ))
            except (IndexError, ValueError):
                await self.bot.say("Sorry, no results.")

    @commands.command(pass_context=True)
    async def rule34(self, ctx, *tags: str):
        """
        For all your non-furry porn needs - Part 2!
        """
        if ctx.message.channel.id in json.load(open('config.json'))["r18"]:
            tags = " ".join(tags).split(" ")
            no_preview = False
            if "no-preview" in tags:
                tags.remove("no-preview")
                no_preview = True
            payload = {
                "limit": 100,
                "tags": " ".join(tags)
            }
            r34 = requests.get(
                "http://rule34.xxx/index.php?page=dapi&s=post&q=index",
                params=payload
            )

            root = ET.fromstring(r34.text)

            try:
                selected_post = root[randrange(len(root))]
                if no_preview:
                    direct_url = "<http:{}>".format(selected_post.attrib["file_url"])
                else:
                    direct_url = "http:{}".format(selected_post.attrib["file_url"])

                await self.bot.say("""{}
    <http://rule34.xxx/index.php?page=post&s=view&id={}>""".format(
                    direct_url,
                    selected_post.attrib["id"]
                ))
            except (IndexError, ValueError):
                await self.bot.say("Sorry, no results.")


def setup(bot):
    bot.add_cog(NSFW(bot))
