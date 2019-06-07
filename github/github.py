import re
from discord.ext import commands

def __init__(self, bot):  # in the class init
    self.coll = bot.plugin_db.get_partition(self)

class Github(commands.Cog):


    @commands.Cog.listener()
    async def on_message(self, message):
        match = re.match(r'plugins#(\d+)', message.content)
        if match:
            issue_num = match.group(1)
            await message.channel.send(f'https://github.com/snaildos/modmail-plugins/issues/{issue_num}')

    @commands.Cog.listener()
    async def on_message(self, message):
        match = re.match(r'harddisk#(\d+)', message.content)
        if match:
            issue_num = match.group(1)
            await message.channel.send(f'https://github.com/snaildos/SnailDOS-Hard-Disk-Repair/issues/{issue_num}')


def setup(bot):
    bot.add_cog(Github())
