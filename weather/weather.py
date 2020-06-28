from redbot.core import commands
import aiohttp
import asyncio
import json
import discord

class Weather(commands.Cog):
    """Get the day's weather or other information"""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()
    @commands.group()
    async def weather(self, ctx):
        """Get the weather of a specified area"""
        pass
    @weather.command()
    async def zip(self, ctx, zip_code:str):
        """Get the weather of a city/town by its zip code"""
        # Code:
        async with aiohttp.ClientSession() as session:
            url = "http://api.openweathermap.org/data/2.5/weather?zip=" + zip_code + "&appid=168ced82a72953d81d018f75eec64aa0&units=imperial"
            async with session.get(url) as response:
                weather_response = await response.json()
            # await ctx.send(f"\n__**Geographical info:**__ \nSpecified City: {weather_response['name']}\nLongitude: {weather_response['coord']['lon']}\nLatitude: {weather_response['coord']['lat']}\n__**Temperature**__ Info:\nCurrent Temp: {weather_response['main']['temp']}\nFeels Like: {weather_response['main']['feels_like']}\nDaily High: {weather_response['main']['temp_max']}\nDaily Low: {weather_response['main']['temp_min']}\n__**Wind Info:")
            embed = discord.Embed(
                    title=f"Weather in {weather_response['name']}, {weather_response['sys']['country']}",
                    description=weather_response['weather'][0]['main'],
                    color=0x0276FD,
            )
            embed.add_field(name='Location:', value=f"**City:** {weather_response['name']}\n**Longitude:** {weather_response['coord']['lon']}\n **Latitude:** {weather_response['coord']['lat']}", inline=False)
            embed.add_field(name='Weather', value=f"Current Temp: {weather_response['main']['temp']}\nFeels Like: {weather_response['main']['feels_like']}\n**Daily High:** {weather_response['main']['temp_max']}\n**Daily Low:** {weather_response['main']['temp_min']}", inline=False)
            embed.set_thumbnail(url=f"https://openweathermap.org/img/wn/{weather_response['weather'][0]['icon']}@2x.png")
            embed.set_footer(text='Starry | discord.gg/7mSqpXN', icon_url=f"https://openweathermap.org/img/wn/{weather_response['weather'][0]['icon']}@2x.png")
            await ctx.send(embed=embed)
