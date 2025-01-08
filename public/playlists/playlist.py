from facade.storage.storage import Storage
from enum import Enum

from typing_extensions import Optional, Final

import json

from discord import Interaction, Member

class Dir(Enum):
    public = "public"
    private = "private"


class PlayList:
    FILE:Final[str] = "playlists.json"
    key:str
    UNICODE:Final[str] = "utf-8"

    users_with_playlists:list[dict]
    selected_playlist:list[dict]
    is_playlist_exists:bool

    def __init__(self,*,playlist_key:str, dir:Dir):
        self.key = playlist_key
        self.storage = Storage(f"playlist/{dir.value}")
        self.users_with_playlists = json.loads(self.storage.get_file(self.FILE).read())
        self.selected_playlist = self.get_selected_playlist()
     
        
    def get_selected_playlist(self) -> list[dict]:    
        for obj in self.users_with_playlists:
            if self.key in obj["playlists"]:
                self.is_playlist_exists = True
                return obj["playlists"][self.key]
        self.is_playlist_exists = False

    def get_all_users_and_playlists(self) -> list[dict]:
        return [
            {"user_id": obj["user_id"], "playlist": obj["playlists"].keys()}
            for obj in self.users_with_playlists
        ]
    
    def get_user(self, interaction:Interaction) -> Member:
        def found_user() -> Optional[dict]:
            for obj in self.users_with_playlists:
                if self.key in obj["playlists"].keys():
                    return obj
            
        user = found_user()

        return interaction.guild.get_member(user["user_id"])
    
    def get_pagination(self,page:int,*,length_get_playlists = 5) -> tuple[int,list[dict]]:
        if page < 1:
            raise ValueError("The page number must be greater than or equal to 1.")
    
        start_index = (page - 1) * length_get_playlists
        end_index = start_index + length_get_playlists
        
        playlists = self.selected_playlist

        count_pages = round(len(playlists) / length_get_playlists)

        return (count_pages,playlists[start_index:end_index])

    def get_music_id(self,id:int) -> dict:
        for music in self.selected_playlist:
            if music["id"] is id:
                return music

    def is_user_id(self,id: int) -> bool:
        return any(user_with_playlist["user_id"] == id for user_with_playlist in self.users_with_playlists)

    def is_music_id(self,id:int) -> bool:
        return any(music["id"] == id for music in self.selected_playlist)

    def insert_playlist(self,data:dict):
        increment_id = len(self.selected_playlist) + 1
        data.update({"id":increment_id})
        self.selected_playlist.append(data)

    def update_playlist(self,id:int,data:dict):
        self.get_music_id(id).update(data)

    def delete_playlist(self,id:int):
        data = self.get_music_id(id)
        self.selected_playlist.remove(data)

    def execute_operations_json(self):
        json_b = json.dumps(self.users_with_playlists,indent=4).encode(self.UNICODE)
        self.storage.upload(json_b,self.FILE)
        self.users_with_playlists = json.loads(self.storage.get_file(self.FILE).read())

    def create_playlist_key(self,interaction: Interaction):
        user_id = interaction.user.id
        if not self.is_user_id(user_id):
            self.users_with_playlists.append({
                "user_id": user_id,
                "playlists": {
                    self.key : []
                }
            })
            return
        for user_with_playlist in self.users_with_playlists:
            if user_with_playlist["user_id"] == user_id:
                user_with_playlist["playlists"].update({self.key:[]})

    def update_playlist_key(self,update_to:str):
        playlist = self.selected_playlist
        for obj in self.users_with_playlists:
            if self.key in obj["playlists"]:
                del obj["playlists"][self.key]
                obj["playlists"].update({update_to:playlist})

    def delete_playlist_key(self):
        for obj in self.users_with_playlists:
            if self.key in obj["playlists"]:
                del obj["playlists"][self.key]
