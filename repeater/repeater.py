    import discord
from discord.ext import com

  @com.command()
    async def say(self, ctx, *, message: commands.clean_content):
        await ctx.send(message)