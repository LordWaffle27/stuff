from redbot.core import commands, bank
import discord


def check_global_setting_admin():
    async def predicate(ctx):
        author = ctx.author
        if not await bank.is_global():
            if not isinstance(ctx.channel, discord.abc.GuildChannel):
                return False
            if await ctx.bot.is_owner(author):
                return True
            if author == ctx.guild.owner:
                return True
            if ctx.channel.permissions_for(author).manage_guild:
                return True
            admin_roles = set(await ctx.bot.get_admin_role_ids(ctx.guild.id))
            for role in author.roles:
                if role.id in admin_roles:
                    return True
        else:
            return await ctx.bot.is_owner(author)

    return commands.check(predicate)


def wallet_disabled_check():
    async def predicate(ctx):
        if await bank.is_global():
            return await ctx.bot.get_cog("Starry").config.disable_wallet()
        if ctx.guild is None:
            return False
        return await ctx.bot.get_cog("Starry").config.guild(ctx.guild).disable_wallet()

    return commands.check(predicate)


def roulette_disabled_check():
    async def predicate(ctx):
        if await bank.is_global():
            return await ctx.bot.get_cog("Starry").config.roulette_toggle()
        if ctx.guild is None:
            return False
        return await ctx.bot.get_cog("Starry").config.guild(ctx.guild).roulette_toggle()

    return commands.check(predicate)