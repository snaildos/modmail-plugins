import re
from core import checks
from core.models import PermissionLevel
from discord.ext import commands



class moderator(commands.Cog):
    def __init__(self, bot):
        self.bot: discord.Client = bot
        self.db = bot.plugin_db.get_partition(self)

    @commands.command()
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def logchannel(self, ctx, channel: discord.TextChannel):
        """Set up a logchannel for the mod logs.
        Usage:
        {prefix}logchannel #channel
        """

        await self.db.find_one_and_update(
            {"_id": "config"},
            {"$set": {"logs": {"channel": str(channel.id)}}},
            upsert=True,
        )
        await ctx.send(f"{channel.mention} is now set up for moderation logs!")

def setup(bot):
    bot.add_cog(moderator(bot))
