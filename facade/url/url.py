from aiohttp import ClientSession, ClientResponseError
from io import BytesIO

from validators import url, ValidationError

class Url:
    def __init__(self,url:str):
        self.url = url    

    def is_url(self) -> bool:
        result = url(self.url)
        if isinstance(result, ValidationError):
            return False
        return True

    async def download(self) -> bytes:
        async with ClientSession() as session:
            async with session.get(self.url) as resp:
                if resp.status != 200:
                    raise ClientResponseError(request_info=resp.request_info,history=resp.history,)
                return BytesIO(await resp.read()).getvalue()