import re
from discord.ext import commands


class Repeater(commands.Cog):


   @commands.command()
    async def say(self, ctx, *, message: commands.clean_content):
        """Follows what you say!!!"""
        await ctx.send(message)



def setup(bot):
    bot.add_cog(Repeater())
