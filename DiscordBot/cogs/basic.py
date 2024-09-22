import nextcord
from nextcord.ext import commands
import json
import requests
import discord
import os
import base64
from requests import post


class basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")



    @commands.command()
    async def video(self, ctx, *args):
        await ctx.message.delete()
        word = ""
        count = 0
        if len(args) > 1:
            for i in args:
                if count == len(args) - 1:
                    word = word + i
                else:
                    word = word + i + '+'
                    count = count + 1
        else:
            word = args[0]

        response = requests.get(f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={word}&key=___")

        videoID = response.json()['items'][0]['id']['videoId']
        await ctx.send(f"https://www.youtube.com/watch?v={videoID}")




    @commands.command()
    async def stock(self, ctx, arg):

        await ctx.message.delete()

        response = requests.get(f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={arg}&apikey=___")

        print(response.json())
        symbol = response.json()["Global Quote"]["01. symbol"]
        opening = float(response.json()["Global Quote"]["02. open"])
        high = float(response.json()["Global Quote"]["03. high"])
        low = float(response.json()["Global Quote"]["04. low"])
        price = float(response.json()["Global Quote"]["05. price"])
        changePercent = response.json()["Global Quote"]["10. change percent"]

        if changePercent[0] == '-':
            embed = discord.Embed(title=symbol, color=0xD2042D)
        else:
            embed = discord.Embed(title=symbol, color=0x7CFC00)

        embed.add_field(name='', value=f"Open: {round(opening, 2)}", inline=True)
        embed.add_field(name='', value=f"High: {round(high, 2)}", inline=False)
        embed.add_field(name='', value=f"Low: {round(low, 2)}", inline=False)
        embed.add_field(name='', value=f"Price: {round(price, 2)}", inline=False)
        embed.add_field(name='', value=f"Change Percent: {changePercent}", inline=False)
        await ctx.send(embed=embed)

        print(symbol)
        print(opening)
        print(high)
        print(low)
        print(price)
        print(changePercent)


    @commands.command()
    async def photo(self, ctx, *args):
        await ctx.message.delete()
        word = ""
        count = 0
        if len(args) > 1:
            for i in args:
                if count == len(args) - 1:
                    word = word + i
                else:
                    word = word + i + '+'
                    count = count + 1
        else:
            word = args[0]


        response = requests.get(f"https://api.pexels.com/v1/search?query={word}&count=1", headers={"Authorization":"___"})
        await ctx.send(response.json()["photos"][0]["src"]["large2x"])



    @commands.command()
    async def weather(self, ctx, *args):
        await ctx.message.delete()
        word = ""
        count = 0
        if len(args) > 1:
            for i in args:
                if count == len(args) - 1:
                    word = word + i
                else:
                    word = word + i + '+'
                    count = count + 1
        else:
            word = args[0]

        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={word}&appid=___")


        description = response.json()["weather"][0]["description"].title()
        currentTemp = round((response.json()["main"]["temp"] - 273.15) * (9.0/5.0) + 32.0, 0)
        high = round((response.json()["main"]["temp_max"] - 273.15) * (9.0/5.0) + 32.0, 0)
        low = round((response.json()["main"]["temp_min"] - 273.15) * (9.0/5.0) + 32.0, 0)
        humidity = response.json()["main"]["humidity"]
        feels = round((response.json()["main"]["feels_like"] - 273.15) * (9.0/5.0) + 32.0, 0)
        wind = response.json()["wind"]["speed"]
        name = response.json()['name']

        embed = discord.Embed(title=name, description=description, color=0x6495ED)

        embed.add_field(name="", value=f"Current Temperature: {currentTemp}°F", inline=True)
        embed.add_field(name="", value=f"Feels Like: {feels}°F", inline=False)
        embed.add_field(name="",value=f"High: {high}°F", inline=False)
        embed.add_field(name="",value=f"Low: {low}°F", inline=False)
        embed.add_field(name="",value=f"Humidity: {humidity}%", inline=False)
        embed.add_field(name="",value=f"Wind: {wind} MPH", inline=False)
        await ctx.send(embed=embed)


    @commands.command()
    async def define(self, ctx, *args):
        await ctx.message.delete()
        word = args[0]

        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        print(response.json()[0])

        embed = discord.Embed(title=f"{response.json()[0]['word'].title()}", color=0x6495ED)

        for i in range(len(response.json()[0]['meanings'])):
            embed.add_field(name="", value=f"{response.json()[0]['meanings'][i]['partOfSpeech']}", inline=False)
            embed.add_field(name="", value=f"{response.json()[0]['meanings'][i]['definitions'][0]['definition']}", inline=False)
            print(response.json()[0]['meanings'][i]['partOfSpeech'])
            print(response.json()[0]['meanings'][i]['definitions'][0]['definition'])

        await ctx.send(embed=embed)


    @commands.command()
    async def wiki(self, ctx, *args):
        await ctx.message.delete()
        word = ""
        count = 0
        if len(args) > 1:
            for i in args:
                if count == len(args) - 1:
                    word = word + i
                else:
                    word = word + i + '+'
                    count = count + 1
        else:
            word = args[0]

        language_code = 'en'
        search_query = word
        number_of_results = 1
        headers = {
        'Authorization': '___',
        'User-Agent': 'DiscordBot'
        }

        base_url = 'https://api.wikimedia.org/core/v1/wikipedia/'
        endpoint = '/search/page'
        url = base_url + language_code + endpoint
        parameters = {'q': search_query, 'limit': number_of_results}
        response = requests.get(url, headers='', params=parameters)
        id = response.json()['pages'][0]['id']
        await ctx.send(f"https://en.wikipedia.org/w/index.php?curid={id}")






    @commands.command()
    async def info(self, ctx):
        await ctx.message.delete()

        embed = discord.Embed(title='Commands', description="Replace the brackets and text with your search", color=0xFFFF00)

        embed.add_field(name="!ping", value="Bot Responds 'Pong!'", inline=True)
        embed.add_field(name="!video [title]", value="Search For Youtube Video", inline=False)
        embed.add_field(name="!photo [name]", value="Search For Any Photo", inline=False)
        embed.add_field(name="!music [name] BY [artist]", value="Returns Spotify Result", inline=False)
        embed.add_field(name="!stock [symbol]", value="Returns Stock Data By Symbol", inline=False)
        embed.add_field(name="!weather [city]", value="Returns Weather Data By City", inline=False)
        embed.add_field(name="!define [word]", value="Returns Definition of Word", inline=False)
        embed.add_field(name="!wiki [search]", value="Returns Wiki Article By Search", inline=False)
        embed.add_field(name="Passive Anti-Cursing", value="Prevents Users From Swearing", inline=False)

        await ctx.send(embed=embed)


    @commands.command()
    async def music(self, ctx, *args):

        await ctx.message.delete()

        word = ""
        count = 0
        if len(args) > 1:
            for i in args:
                if count == len(args) - 1:
                    word = word + i
                else:
                    word = word + i + '+'
                    count = count + 1
        else:
            word = args[0]


        end = word.find('BY')

        if end == -1:
            song = word
        else:
            song = word[0:end - 1]
            artist = word[end + 3:len(word)]


        auth_string = '___'
        auth_bytes = auth_string.encode("utf-8")
        auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": "Basic " + auth_base64,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {"grant_type": "client_credentials"}
        response = post(url, headers=headers, data=data)
        result = json.loads(response.content)
        token = result["access_token"]

        headers2 = {
            "Authorization": f'Bearer {token}'
        }

        if end == -1:
            spotify = requests.get(f"https://api.spotify.com/v1/search?q={song}&type=track&limit=1", headers=headers2)
            songID = spotify.json()['tracks']['items'][0]['id']
            await ctx.send(f'https://open.spotify.com/track/{songID}')
        else:
            spotify = requests.get(f"https://api.spotify.com/v1/search?q=track%20{song}+artist%20{artist}&type=track&limit=1", headers=headers2)
            songID = spotify.json()['tracks']['items'][0]['id']
            await ctx.send(f'https://open.spotify.com/track/{songID}')



    @commands.Cog.listener()
    async def on_message(ctx, message):

        curseWords = ['damn', 'yale']

        if message.author.id == 862784768462028820:
            return

        if any(word in message.content.lower() for word in curseWords):
            await message.delete()












def setup(bot):
    bot.add_cog(basic(bot))
