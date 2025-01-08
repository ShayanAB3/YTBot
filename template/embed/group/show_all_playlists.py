from template.embed.embed import Embed
from discord import Embed as DiscordEmbed, Color, Interaction, Member

class ShowAllPlaylist(Embed):
    all_users_and_playlists:list[dict]
    interaction:Interaction

    title="All playlists"
    description="This all playlists. You can show selected playlist. \nCommand: **public-playlist show** `playlists_key`."
    color=Color.red()

    def template(self, embed:DiscordEmbed, data:dict):
        embed.set_author(icon_url=self.interaction.user.avatar.url,
                         name=self.interaction.user.display_name)
        
        for user_with_playlist in self.all_users_and_playlists:
            author_playlist:Member = self.interaction.guild.get_member(user_with_playlist["user_id"])
            nick_name = author_playlist.nick or author_playlist.name

            playlists_keys = list(user_with_playlist['playlist'])
            mapped_playlists = list(map(lambda key: f"{playlists_keys.index(key)+1}. ```{key}```\n", playlists_keys))
            str_list_playlist = "".join(mapped_playlists)

            embed.add_field(
                name=f"Author: {nick_name}",
                value=f"Playlists key: \n{str_list_playlist}",
                inline=False
            )