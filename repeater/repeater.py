import re
from discord.ext import commands

def emoji:
    base = 0x1F1E6


class Repeater(commands.Cog):


    @commands.command()
    async def say(self, ctx, *, message: commands.clean_content):
        """Copys what you say"""
        send = await ctx.send(message)
        await send.add_reaction(emoji)


def setup(bot):
    bot.add_cog(Repeater(bot))
