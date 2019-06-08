import re
from discord.ext import commands


class Repeater(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)



    @commands.Cog.listener()
    async def say(self, ctx, *, message: commands.clean_content):
        await ctx.send(message)



def setup(bot):
    bot.add_cog(Repeater())
