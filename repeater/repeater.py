import re
from discord.ext import commands

def to_emoji(c):
    base = 0x1F1E6
    return chr(base + c)


class Repeater(commands.Cog):


    @commands.command()
    async def say(self, ctx, *, message: commands.clean_content):
        """Copys what you say"""
        actual_poll = await ctx.send(message)
        await actual_poll.add_reaction(to_emoji)


def setup(bot):
    bot.add_cog(Repeater(bot))
