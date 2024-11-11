import yt_dlp
from public.api.yt_dlp.yt_dlp_parser import YTDlpParser

from discord import Embed, Color

class YTDlp:
    YDL_OPTIONS = {'format':'bestaudio',
                   'noplaylist': True,
                    'writesubtitles':False}

    def __init__(self, YDL_OPTIONS: dict = YDL_OPTIONS):
        self.YDL_OPTIONS = YDL_OPTIONS
    
    def get_parser(self,info: dict[str]):
        parser = YTDlpParser(info)
        return parser.get()

    def url(self,url:str):
        with yt_dlp.YoutubeDL(self.YDL_OPTIONS) as ydl:
           info = ydl.extract_info(url, download=False)
           return self.get_parser(info)

    def search(self,name:str):
        with yt_dlp.YoutubeDL(self.YDL_OPTIONS) as ydl:
            info = ydl.extract_info(f"ytsearch:{name}", download=False)
            return self.get_parser(info)
        
    def embed(info: dict[str])-> Embed:
        embed = Embed(
            title=info.get("title"),
            description=info.get("channel"),
            color=Color.red(),
            url=info.get("webpage_url")
        )
        embed.set_author(name="YouTube", url=info.get("webpage_url"))
        embed.set_image(url=info.get("thumbnail"))
        return embed
    
    def list_music_embed(data:list[dict[str]])-> Embed:
        if not data:
            embed = Embed(
            title="**Quere is empty**",
            description="There is no music to play",
            color=Color.red(),
            )
            return embed

        embed = Embed(
        title="**Music added to queue:**",
        description=f"**Count music: ** `{len(data)}`\nList music: ",
        color=Color.red(),
        )
        for info in data:
            embed.add_field(name=info["title"], value=f"{info["channel"]}",inline=False)
        return embed