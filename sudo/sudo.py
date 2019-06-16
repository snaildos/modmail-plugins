import sys
import discord
from discord.ext import commands



class sudo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def sudo(self, ctx, member: discord.Member, *, msg):
        """
    Make a user say something
        """

        webhook = await ctx.channel.create_webhook(name="su")
        await webhook.send(content=msg, username=member.name, avatar_url=member.avatar_url)
        await webhook.delete()

        message = ctx.message
        message.author = member
        message.content = msg
        await bot.process_commands(message)


def setup(bot):
    bot.add_cog(sudo(bot))