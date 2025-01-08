from cogs.group.group import Group
from discord import Interaction, Embed, Color
from discord.ext.commands import Bot
from discord.ui import View

from template.ui.paginate.paginate import Paginate

from template.embed.group.manage_playlist import ManagePlaylist
from template.embed.group.show_all_playlists import ShowAllPlaylist

from public.playlists.playlist import PlayList, Dir

from route.route import route

from public.api.yt_dlp.yt_dlp import YTDlp


class PublicPlayListCog(Group):
    """
    name: Union[:class:`str`, :class:`locale_str`]
        The name of the group. If not given, it defaults to a lower-case
        kebab-case version of the class name.
    """
    name = "public-playlist"
    
    """
    description: Union[:class:`str`, :class:`locale_str`]
        The description of the group. This shows up in the UI to describe
        the group. If not given, it defaults to the docstring of the
        class shortened to 100 characters.
    """
    description = "This is a public playlist. Use it to easily browse and organize your chosen playlists."

    OPTIONS_YTDLP = {
        'extract_flat': True,
        'noplaylist': True,
        'writesubtitles':False
    }

    @route.slash.command(name="show_all", description="Show all public playlist")
    async def show_all(self, interaction:Interaction):
        playlist_manage = PlayList(playlist_key="",dir=Dir.public)

        embed = ShowAllPlaylist()
        embed.all_users_and_playlists = playlist_manage.get_all_users_and_playlists()
        embed.interaction = interaction

        await interaction.response.send_message(embed=embed.get(), ephemeral=True,delete_after=180)


    @route.slash.command(name="show", description="Show selected playlist")
    @route.slash.describe(playlist="Select playlist key")
    async def show(self, interaction: Interaction, playlist:str, page:int=1):
        playlist_manage = PlayList(playlist_key=playlist,dir=Dir.public)
        if not playlist_manage.is_playlist_exists:
            await interaction.response.send_message(f"**Your selected playlist not exists**\nYour selected playlist: **{playlist}**")
            return

        (count_pages,playlists) = playlist_manage.get_pagination(page,length_get_playlists=10)
        
        user = playlist_manage.get_user(interaction)
        nick_name = user.nick or user.name

        embed = ManagePlaylist()
        embed.title=f"Playlist: {playlist}"
        embed.description += f"\n## Page: {page}"
        embed.description += f"\n### Author: {nick_name}\n"
        embed.interaction = interaction
        embed.playlists = playlists

        view = View()

        paginate = Paginate(count_pages)
        paginate.group = self.name
        paginate.command = "show"
        paginate.args = {"playlist":playlist}
        paginate.generate(view)

        await interaction.response.send_message(embed=embed.get(),view=view,ephemeral=True,delete_after=180)
    
    
    @route.slash.command(name="add",description="Adding music selected playlist")
    @route.slash.describe(playlist="Select playlist key", name_or_url="Insert name or url your music")
    async def add_playlist(self,interaction:Interaction,playlist:str,name_or_url:str):
        ytdlp = YTDlp(self.OPTIONS_YTDLP)
        playlist_manage = PlayList(playlist_key=playlist ,dir=Dir.public)

        if not playlist_manage.is_playlist_exists:
            await interaction.response.send_message(f"**Your selected playlist not exists**\nYour selected playlist: **{playlist}**")
            return
        
        await interaction.response.defer()

        try:
            search_results = ytdlp.search_or_url(name_or_url)

            if not search_results:
                await interaction.followup.send("**Could not find the video on request.**", ephemeral=True,delete_after=180)
                return

            result = {
                "title":search_results["title"],
                "channel": search_results["channel"],
                "thumbnail":search_results["thumbnail"],
                "webpage_url": search_results["webpage_url"]
            }
            playlist_manage.insert_playlist(result)
            playlist_manage.execute_operations_json()

            await interaction.followup.send("**Music has been added**", ephemeral=True)
        except Exception as e:
            embed = Embed(title=e.__class__.__name__,
                          color=Color.red(),
                          description=e.__str__())
            await interaction.followup.send(embed=embed, ephemeral=True)

    @route.slash.command(name="update",description="Updating selected music")
    @route.slash.describe(playlist="Select playlist key",id="Select id for indentification music" ,name_or_url="Insert name or url your music")
    async def update_playlist(self,interaction: Interaction,playlist:str,id:int,name_or_url:str):
        ytdlp = YTDlp(self.OPTIONS_YTDLP)
        playlist_manage = PlayList(playlist_key=playlist ,dir=Dir.public)
        
        if not playlist_manage.is_playlist_exists:
            await interaction.response.send_message(f"**Your selected playlist not exists**\nYour selected playlist: **{playlist}**")
            return
        
        if not playlist_manage.is_music_id(id):
            await interaction.response.send_message("**Not found your music.**",ephemeral=True,delete_after=180)
            return

        await interaction.response.defer()
        try:
            search_results = ytdlp.search_or_url(name_or_url)

            if not search_results:
                await interaction.followup.send("**Could not find the video on request.**", ephemeral=True)
                return
            
            result = {
                "title":search_results["title"],
                "channel": search_results["channel"],
                "webpage_url": search_results["webpage_url"]
            }
            playlist_manage.update_playlist(id,result)
            playlist_manage.execute_operations_json()

            await interaction.followup.send("**Music has been updated**", ephemeral=True)
        except Exception as e:
            embed = Embed(title=e.__class__.__name__,
                          color=Color.red(),
                          description=e.__str__())
            await interaction.followup.send(embed=embed, ephemeral=True,delete_after=180)

    @route.slash.command(name="delete", description="Deleting selected music")
    @route.slash.describe(playlist="Select playlist key",id="Select id for indentification music")
    async def delete_playlist(self,interaction: Interaction,playlist:str,id:int):
        playlist_manage = PlayList(playlist_key=playlist ,dir=Dir.public)

        if not playlist_manage.is_playlist_exists:
            interaction.response.send_message(f"**Your selected playlist not exists**\nYour selected playlist: **{playlist}**")
            return

        if not playlist_manage.is_music_id(id):
            await interaction.response.send_message("**Not found your music**",ephemeral=True,delete_after=180)
            return
        
        playlist_manage.delete_playlist(id)
        playlist_manage.execute_operations_json()

        await interaction.response.send_message("**Music has been deleted**",ephemeral=True)
            

async def setup(bot: Bot):
    bot.tree.add_command(PublicPlayListCog(bot))