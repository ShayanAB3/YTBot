import yt_dlp
from public.api.yt_dlp.yt_dlp_parser import YTDlpParser

from facade.url.url import Url

class YTDlp:
    YDL_OPTIONS = {'format':'bestaudio',
                   'noplaylist': True,
                    'writesubtitles':False}

    def __init__(self, YDL_OPTIONS: dict = YDL_OPTIONS):
        self.YDL_OPTIONS = YDL_OPTIONS
    
    def search_or_url(self,name_or_url:str):
        url = Url(name_or_url)
        if url.is_url():
            return self.url(name_or_url)
        return self.search(name_or_url)

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