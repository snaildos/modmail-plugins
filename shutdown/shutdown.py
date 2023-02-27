import sys
import discord
import logging
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

logger = logging.getLogger('Modmail')


class shutdown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.has_permissions(PermissionLevel.OWNER)
    async def shutdown(self, ctx):
        """Shutdown the bot"""
        msg = await ctx.send(embed=discord.Embed(
            color=discord.Color.blurple(),
            description="Winding down...."
        ))

        await ctx.invoke(self.bot.get_command('debug clear'))
        emsg = await msg.edit(embed=discord.Embed(
            color=discord.Color.blurple(),
            description="Clearing Debug Cache..."
        ))
        logger.info("==== Shutting down bot ====")
        await msg.edit(embed=discord.Embed(
            color=discord.Color.blurple(),
            description="Cleared Debug Cache! \n \n Sucessful Shutdown!"
        ))
        await self.bot.close()

async def setup(bot):
    await bot.add_cog(shutdown(bot))
