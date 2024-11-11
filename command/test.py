from discord.ext import commands
from route.route import route
from discord import Embed, Color

@route.prefix.command(name="test")
async def test(ctx: commands.Context):
    data = [
        {"title": "𝐒𝐓𝐀𝐋𝐈𝐍𝐆𝐑𝐀𝐃 - 𝐓𝐡𝐞 𝐏𝐞𝐫𝐟𝐞𝐜𝐭 𝐆𝐢𝐫𝐥 𝐄𝐝𝐢𝐭",
        "channel":"busman",
        "channel_url":"https://www.youtube.com/channel/UCpq9wauNSxEw-bksVLrmzxw",
        "thumbnail": "https://i.ytimg.com/vi_webp/T6ezlkBof4Q/maxresdefault.webp",
        "webpage_url":"https://www.youtube.com/watch?v=T6ezlkBof4Q"},

        {"title": "Narvent - Her Eyes (4K Music Video)",
        "channel":"Narvent",
        "channel_url":"https://www.youtube.com/channel/UC5yQIaYVVhKH8HHZgjA_IVg",
        "thumbnail": "https://i.ytimg.com/vi_webp/cIhNXNR27Sc/maxresdefault.webp",
        "webpage_url":"https://www.youtube.com/watch?v=cIhNXNR27Sc"},
    ]
    embed = Embed(
        title="**List music**",
        description=f"**Count music: ** `{len(data)}`",
        color=Color.red(),
    )
    for info in data:
        embed.add_field(name=info["title"], value=f"{info["channel"]}",inline=False)
    await ctx.send(embed=embed)
    
    
async def setup(bot:commands.Bot):
    bot.add_command(test)