import discord
from discord.ext import tasks, commands

class Sample(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.loopDaily.start()
    
    @tasks.loop(hours=24)
    async def loopDaily(self, ctx):
        await ctx.send('This loops once a day!')
    
    @loopDaily.before_loop()
    async def before_loopDaily(self, ctx):
        # this runs right before loopDaily
        await self.bot.wait_until_ready()

    @commands.command()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def test(self, ctx):
        await ctx.send('this is a test command from a Cog!')

def setup(bot):
    bot.add_cog(Sample(bot))