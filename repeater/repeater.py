from discord.ext import commands
import asyncio


class Repeater(commands.Cog):


    @commands.command()
    async def say(self, ctx, *, message: commands.clean_content):
        await ctx.send(message)



def setup(bot):
    bot.add_cog(Repeater())
