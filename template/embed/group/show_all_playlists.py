from template.embed.embed import Embed
from discord import Embed as DiscordEmbed, Color, Interaction, Member

from sqlalchemy.orm import Query

from public.orm.models.playlist import Playlist

from json import loads

class ShowAllPlaylist(Embed):
    playlists:list[Playlist]
    interaction:Interaction

    title="All playlists"
    description="This all playlists. You can show selected playlist. \nCommand: **public-playlist show** `playlists_key`."
    color=Color.red()

    def template(self, embed:DiscordEmbed, data:dict):
        embed.set_author(icon_url=self.interaction.user.avatar.url,
                         name=self.interaction.user.display_name)
        
        for playlist in self.playlists:
            author_playlist:Member = self.interaction.guild.get_member(playlist.author_id)
            nick_name = author_playlist.nick or author_playlist.name

            str_list_playlist = "".join(f"```{name}```\n" for name in loads(playlist.names_json))

            embed.add_field(
                name=f"Author: {nick_name}",
                value=f"Playlists key: \n{str_list_playlist}",
                inline=False
            )