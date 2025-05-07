from cogs.group.group import Group
from route.route import route

from discord import Interaction
from discord.ext.commands import Bot

from public.orm.models.playlist import Playlist
from public.orm.models.track import Track

from public.orm.session import session

class PublicPlayListManageCog(Group):
    name="public-playlist-manage"
    description = "This group manages playlists: create, edit, delete."

    @route.slash.command(name="create",description="Creating new playlist")
    @route.slash.describe(playlist="Select playlist key")
    @route.slash.guild_only()
    async def create(self,interaction:Interaction,playlist:str):
        playlist_model = session.query(Playlist).filter_by(server_id=interaction.guild_id,name=playlist).first()
        if playlist_model:
            await interaction.response.send_message(f"** Playlist: {playlist} is exists **", ephemeral=True,delete_after=180)
            return
        
        new_playlist = Playlist()
        new_playlist.name = playlist
        new_playlist.author_id = interaction.user.id
        new_playlist.server_id = interaction.guild_id
        session.add(new_playlist)
        session.commit()

        await interaction.response.send_message(f"** Playlist {playlist} has beed created **",ephemeral=True,delete_after=180)
    
    @route.slash.command(name="update",description="Updating playlist key")
    @route.slash.describe(playlist="Select playlist key", update_to="Enter the changed playlist")
    async def update(self,interaction: Interaction,playlist:str,update_to:str):
        playlist_model = session.query(Playlist).filter_by(server_id=interaction.guild_id,name=playlist).first()
        if not playlist_model:
            await interaction.response.send_message(f"** Playlist: {playlist} is not exists **", ephemeral=True,delete_after=180)
            return
        
        playlist_model.name = playlist
        session.commit()

        await interaction.response.send_message(f"** Playlist key {playlist} has been updated to {update_to} **", ephemeral=True,delete_after=180)
    
    @route.slash.command(name="delete",description="Deleting playlist")
    @route.slash.describe(playlist="Select playlist key")
    async def delete(self,interaction: Interaction, playlist:str):
        playlist_model = session.query(Playlist).filter_by(server_id=interaction.guild_id,name=playlist).first()
        if not playlist_model:
            await interaction.response.send_message(f"** Playlist: {playlist} is not exists **", ephemeral=True,delete_after=180)
            return
        
        session.query(Track).filter(Track.playlist_id == playlist_model.id).delete()

        session.delete(playlist_model)
        session.commit()
        await interaction.response.send_message(f"** Playlist key {playlist} has been deleted **", ephemeral=True,delete_after=180)

async def setup(bot: Bot):
    bot.tree.add_command(PublicPlayListManageCog(bot))