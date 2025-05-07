from cogs.group.group import Group

from discord import Interaction, Embed, Color
from discord.ext.commands import Bot
from discord.ui import View

from template.ui.paginate.paginate import Paginate

from template.embed.group.manage_playlist import ManagePlaylist
from template.embed.group.show_all_playlists import ShowAllPlaylist

from public.orm.models.playlist import Playlist
from public.orm.models.track import Track

from public.orm.session import session

from route.route import route

from public.api.yt_dlp.yt_dlp import YTDlp

from sqlalchemy import func 

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
    @route.slash.guild_only()
    async def show_all(self, interaction:Interaction):
        playlists:list[Playlist] = session.query(
                Playlist.author_id,
                func.json_arrayagg(Playlist.name).label("names_json"),
                Playlist.server_id
            ).group_by(Playlist.author_id,Playlist.server_id).filter_by(server_id=interaction.guild_id)
        
        embed = ShowAllPlaylist()
        embed.playlists = playlists
        embed.interaction = interaction
    
        await interaction.response.send_message(embed=embed.get(), ephemeral=True,delete_after=180)


    @route.slash.command(name="show", description="Show selected playlist")
    @route.slash.describe(playlist="Select playlist key")
    @route.slash.guild_only()
    async def show(self, interaction: Interaction, playlist:str, page:int=1):
        playlist_model = session.query(Playlist).filter_by(server_id=interaction.guild_id,name=playlist).first()

        if not playlist_model:
            await interaction.response.send_message(f"**Your selected playlist not exists**\nYour selected playlist: **{playlist}**")
            return
        
        page_size = 10

        tracks = session.query(Track).filter_by(playlist_id=playlist_model.id)

        count_pages = (tracks.count() + page_size - 1) // page_size

        playlists = tracks.offset((page-1) * page_size).limit(page * page_size)
        
        author = interaction.guild.get_member(playlist_model.author_id)
        author_nick_name = author.nick or author.name

        embed = ManagePlaylist()
        embed.title=f"Playlist: {playlist}"
        embed.description += f"\n## Page: {page}"
        embed.description += f"\n### Author: {author_nick_name}\n"
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
    @route.slash.guild_only()
    async def add_playlist(self,interaction:Interaction,playlist:str,name_or_url:str):
        ytdlp = YTDlp()
        playlist = session.query(Playlist).filter_by(server_id=interaction.guild_id,name=playlist).first()

        if not playlist:
            await interaction.response.send_message(f"**Your selected playlist not exists**\nYour selected playlist: **{playlist}**")
            return
        
        await interaction.response.defer()

        try:
            search_results = ytdlp.search_or_url(name_or_url)

            if not search_results:
                await interaction.followup.send("**Could not find the video on request.**", ephemeral=True,delete_after=180)
                return
      
            new_track = Track()
            new_track.user_id = interaction.user.id
            new_track.server_id = interaction.guild_id
            new_track.playlist_id = playlist.id
            new_track.title = search_results["title"]
            new_track.channel = search_results["channel"]
            new_track.thumbnail = search_results["thumbnail"]
            new_track.webpage_url = search_results["webpage_url"]
            
            session.add(new_track)
            session.commit()

            await interaction.followup.send("**Music has been added**", ephemeral=True)
        except Exception as e:
            embed = Embed(title=e.__class__.__name__,
                          color=Color.red(),
                          description=e.__str__())
            await interaction.followup.send(embed=embed, ephemeral=True)

    @route.slash.command(name="update",description="Updating selected music")
    @route.slash.describe(playlist="Select playlist key",id="Select id for indentification music" ,name_or_url="Insert name or url your music")
    @route.slash.guild_only()
    async def update_playlist(self,interaction: Interaction,playlist:str,id:int,name_or_url:str):
        ytdlp = YTDlp()
        playlist = session.query(Playlist).filter_by(server_id=interaction.guild_id,name=playlist).first()
        
        if not playlist:
            await interaction.response.send_message(f"**Your selected playlist not exists**\nYour selected playlist: **{playlist}**")
            return
        track = session.query(Track).filter_by(playlist_id=playlist.id,id=id).first()

        if not track:
            await interaction.response.send_message("**Not found your music.**",ephemeral=True,delete_after=180)
            return

        await interaction.response.defer()
        try:
            search_results = ytdlp.search_or_url(name_or_url)

            if not search_results:
                await interaction.followup.send("**Could not find the video on request.**", ephemeral=True)
                return
            
            track.title = search_results["title"]
            track.channel = search_results["channel"]
            track.thumbnail = search_results["thumbnail"]
            track.webpage_url = search_results["webpage_url"]
            session.commit()

            await interaction.followup.send("**Music has been updated**", ephemeral=True)
        except Exception as e:
            embed = Embed(title=e.__class__.__name__,
                          color=Color.red(),
                          description=e.__str__())
            await interaction.followup.send(embed=embed, ephemeral=True,delete_after=180)

    @route.slash.command(name="delete", description="Deleting selected music")
    @route.slash.describe(playlist="Select playlist key",id="Select id for indentification music")
    async def delete_playlist(self,interaction: Interaction,playlist:str,id:int):
        playlist = session.query(Playlist).filter_by(server_id=interaction.guild_id,name=playlist).first()

        if not playlist:
            interaction.response.send_message(f"**Your selected playlist not exists**\nYour selected playlist: **{playlist}**")
            return

        track = session.query(Track).filter_by(playlist_id=playlist.id,id=id).first()

        if not track:
            await interaction.response.send_message("**Not found your music**",ephemeral=True,delete_after=180)
            return
        
        session.delete(track)
        session.commit()

        await interaction.response.send_message("**Music has been deleted**",ephemeral=True)
            

async def setup(bot: Bot):
    bot.tree.add_command(PublicPlayListCog(bot))