from discord.ext import commands
from route.route import route

from facade.url.url import Url

from facade.storage.storage import Storage

@route.prefix.command(name="send_file")
async def send_file(ctx: commands.Context):
    file = Storage(dirname="photos")
    photo_file = file.get("file1.jpg")
    await ctx.send("Here is your file:", file=photo_file)

@route.prefix.command(name="send_file_from_url")
async def send_file_from_url(ctx: commands.Context, url: str):
    urlsrc = Url(url)
    file = Storage("photos")
    data_file = await urlsrc.download()
    file.upload(data_file,"file1.jpg")
    
@route.prefix.command(name="upload")
async def upload_file(ctx: commands.Context):
    if not ctx.message.attachments:
        await ctx.send("Please attach a file.")
        return

    attachment = ctx.message.attachments[0]
    file_content = await attachment.read()
    file = Storage("photos")
    file.upload(file_content,"file2.jpg")

async def setup(bot:commands.Bot):
    bot.add_command(send_file)
    bot.add_command(upload_file)
    bot.add_command(send_file_from_url)