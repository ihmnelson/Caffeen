from discord.ext import commands


async def setup(bot):
    await bot.add_cog(Test(bot))
    print(f'Loaded Cogs in {__file__}')


async def teardown(bot):
    print('Unloaded Primary Features')


class Test(commands.Cog):
    def __int__(self, client):
        self.client = client

    @commands.command(aliases=['invite', 'il'])
    async def invite_link(self, ctx):
        await ctx.send('https://discord.com/api/oauth2/authorize?client_id=964984847787520110&permissions=8&scope=bot')


