from template.ui.modal.modal import Modal

from discord.ui import Modal as DiscordModal, TextInput
from discord import Interaction

from public.api.yt_dlp.yt_dlp import YTDlp
from public.playlists.playlist import PlayList, Dir


class AddMusic(Modal):
    FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
    }

    playlist_key = ""
    playlist_dir:Dir

    title="Add Music"
    items=[TextInput(label="Name or url music",placeholder="Insert url or name music", required=True)]

    async def on_submit(self,modal:DiscordModal,interaction:Interaction):
        name_or_url:str = modal.children[0].value
        ytdlp = YTDlp(self.FFMPEG_OPTIONS)
        await interaction.response.defer()

        search_results = ytdlp.search_or_url(name_or_url)

        if not search_results:
            await interaction.followup.send("**Could not find the video on request.**", ephemeral=True)
            return
        
        playlist = PlayList(playlist_key=self.playlist_key ,dir=self.playlist_dir)
        result = {
            "title":search_results["title"],
            "channel": search_results["channel"],
            "webpage_url": search_results["webpage_url"]
        }
        playlist.insert_playlist(result)

        await interaction.followup.send("**Music has been added**", ephemeral=True)





