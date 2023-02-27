import re
from discord.ext import commands

class Repeater(commands.Cog):

    @commands.command()
    async def say(self, ctx, *, message: commands.clean_content):
        """Copy what you say"""
        await ctx.send(message)


async def setup(bot):
    await bot.add_cog(repeater(bot))
