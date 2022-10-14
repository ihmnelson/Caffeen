from discord.ext import commands
from discord.ext import tasks


async def setup(bot):
    await bot.add_cog(Example(bot))
    print(f'Loaded {__file__}')


async def teardown(bot):
    print(f'Unloaded {__file__}')


class Example(commands.Cog):
    def __int__(self, client):
        self.client = client

    @commands.command(aliases=['ec'], help='Example command in example cog.', hidden=True)
    @commands.guild_only()  # Can also use @commands.dm_only(), here's a full list
    # https://gist.github.com/Painezor/eb2519022cd2c907b56624105f94b190
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def example_command(self, ctx):
        await ctx.send('Hi!')



