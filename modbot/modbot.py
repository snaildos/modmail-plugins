from discord.ext import commands as commands
from core import checks
import discord
from core.models import PermissionLevel


class sudo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_result = None

    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def modbot(self, ctx, *, msg):
        """
       Make modbot say somthing.
        """

        webhook = await ctx.channel.create_webhook(name="su")
        await webhook.send(content=msg, username=DarkSideModbot, avatar_url="https://darksidemc.ga/img/core-img/logo.png")
        await webhook.delete()

        message = ctx.message
        message.content = msg
        await self.bot.process_commands(message)

def setup(bot):
    bot.add_cog(sudo(bot))
