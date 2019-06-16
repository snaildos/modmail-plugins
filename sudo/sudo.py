import discord

from discord.ext import commands

from core import checks

from core.models import PermissionLevel


class sudo(cmd.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_result = None

    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def sudo(self, ctx, member: discord.Member, *, msg):
        """
       Make user say something.
        """

        webhook = await ctx.channel.create_webhook(name="sudo")
        await webhook.send(content=msg, username=member.name, avatar_url=member.avatar_url)
        await webhook.delete()

        message = ctx.message
        message.author = member
        message.content = msg
        await self.bot.process_commands(message)

def setup(bot):
    bot.add_cog(sudo(bot))
