from template.embed.embed import Embed
from discord import Color, Embed as DiscordEmbed, Interaction

from sqlalchemy.orm import Query
from public.orm.models.track import Track

class ManagePlaylist(Embed):
    interaction:Interaction
    playlists:Query[Track]

    description = f"This selected one of the playlists. The playlist has pagination, but pagination will appear if the number of tracks exceeds 10"
    color = Color.red() 
    
    def template(self, embed:DiscordEmbed, data:dict):
        embed.set_author(icon_url=self.interaction.user.avatar.url,name=f"{self.interaction.user.display_name}")
        if self.playlists.count() == 0:
            embed.description += "\n# PlayList empty"
            return
        for music in self.playlists:
            embed.add_field(
                name=f"Id: {music.id}",
                value=f"**Music: {music.title}**\nAuthor: {music.channel}",
                inline=False
            )