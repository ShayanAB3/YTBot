from typing import Optional, Any

class YTDlpParser:
    info:dict[str,Any] = {}
    is_video:bool = False

    def __init__(self,info:dict[str,Any]):
        self.info = info
        self.is_video = self.set_is_video()

    def set_is_video(self) -> bool:
        if "entries" in self.info:
            self.info = self.info["entries"]
            return True
        if "thumbnail" in self.info and "title" in self.info:
            return True
        return False

    def get(self) -> Optional[dict[str,Any]]:
        if not self.is_video:
            return {}
        if isinstance(self.info, list):
            return self.info[0]
        return self.info