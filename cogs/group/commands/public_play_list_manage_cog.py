from cogs.group.group import Group
from route.route import route
from public.playlists.playlist import PlayList, Dir

from discord import Interaction
from discord.ext.commands import Bot

class PublicPlayListManageCog(Group):
    name="public-playlist-manage"
    description = "This group manages playlists: create, edit, delete."

    @route.slash.command(name="create",description="Creating new playlist")
    @route.slash.describe(playlist="Select playlist key")
    async def create(self,interaction:Interaction,playlist:str):
        playlist_manage = PlayList(playlist_key=playlist,dir=Dir.public)
        if playlist_manage.is_playlist_exists:
            await interaction.response.send_message(f"** Playlist: {playlist} is exists **", ephemeral=True,delete_after=180)
            return
        playlist_manage.create_playlist_key(interaction)
        playlist_manage.execute_operations_json()
        await interaction.response.send_message(f"** Playlist {playlist} has beed created **",ephemeral=True,delete_after=180)
    
    @route.slash.command(name="update",description="Updating playlist key")
    @route.slash.describe(playlist="Select playlist key", update_to="Enter the changed playlist")
    async def update(self,interaction: Interaction,playlist:str,update_to:str):
        playlist_manage = PlayList(playlist_key=playlist,dir=Dir.public)
        if not playlist_manage.is_playlist_exists:
            await interaction.response.send_message(f"** Playlist: {playlist} is not exists **", ephemeral=True,delete_after=180)
            return
        playlist_manage.update_playlist_key(update_to)
        playlist_manage.execute_operations_json()
        await interaction.response.send_message(f"** Playlist key {playlist} has been updated to {update_to} **", ephemeral=True,delete_after=180)
    
    @route.slash.command(name="delete",description="Deleting playlist")
    @route.slash.describe(playlist="Select playlist key")
    async def delete(self,interaction: Interaction, playlist:str):
        playlist_manage = PlayList(playlist_key=playlist,dir=Dir.public)
        if not playlist_manage.is_playlist_exists:
            await interaction.response.send_message(f"** Playlist: {playlist} is not exists **", ephemeral=True,delete_after=180)
            return
        playlist_manage.delete_playlist_key()
        playlist_manage.execute_operations_json()
        await interaction.response.send_message(f"** Playlist key {playlist} has been deleted **", ephemeral=True,delete_after=180)

async def setup(bot: Bot):
    bot.tree.add_command(PublicPlayListManageCog(bot))