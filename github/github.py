import re
from discord.ext import commands


class Github(commands.Cog):

    @commands.Cog.listener()
    async def on_message(self, message):
        match = re.match(r'plugins#(\d+)', message.content)
        if match:
            issue_num = match.group(1)
            await message.channel.send(f'https://github.com/snaildos/modmail-plugins/issues/{issue_num}')
            return
        match = re.match(r'harddisk#(\d+)', message.content)
        if match:
            issue_num = match.group(1)
            await message.channel.send(f'gone')


async def setup(bot):
    await bot.add_cog(github(bot))
