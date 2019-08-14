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

        webhook = await ctx.channel.create_webhook(name="DarkSide-ModBot")
        await webhook.send(content=msg, avatar_url="https://cdn.discordapp.com/avatars/591556661018099732/ff09e0cdc176fdd9ea33bafca4a097fc.png?size=128")
        await webhook.delete()

        message = ctx.message
        message.author = member
        message.content = msg
        await self.bot.process_commands(message)

def setup(bot):
    bot.add_cog(sudo(bot))
