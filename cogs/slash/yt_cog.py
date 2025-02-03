from cogs.cogs import Cogs
from discord import Interaction, FFmpegOpusAudio, Embed, Color
from discord.ext.commands import Bot

from route.route import route

from public.api.yt_dlp.yt_dlp import YTDlp
from public.api.yt_dlp.yt_dlp_embed import YTDlpEmbed

from facade.structures_data.queue import Queue

from public.playlists.playlist import PlayList, Dir

class YTCog(Cogs):
    FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
    }
    
    queue_play_list = Queue()

    now_play_info:dict[str,str]
    is_repeat:bool = False

    @route.slash.command(name="join", description="Joins a voice channel")
    async def join(self, interaction:Interaction):
        channel = interaction.user.voice.channel

        if not interaction.user.voice:
            await interaction.response.send_message("**You must be in a voice channel to use this command.**", ephemeral=True,delete_after=180)
            return
        if interaction.guild.voice_client:
            await interaction.response.send_message(f"The bot is already connected to the channel **{channel.name}.**", ephemeral=True,delete_after=180)
            return
        
        await channel.connect()
        await interaction.response.send_message(f"Joined voice channel: **{channel.name}**", ephemeral=True,delete_after=180)
    

    @route.slash.command(name="leave", description="Leaves the voice channel")
    async def leave(self, interaction: Interaction):
        voice_client = interaction.guild.voice_client
        if not voice_client:
            await interaction.response.send_message("**The bot is not in the voice channel.**", ephemeral=True,delete_after=180)
        
        await voice_client.disconnect()
        await interaction.response.send_message("**Left the voice channel.**", ephemeral=True,delete_after=180)


    @route.slash.command(name="play",description="Plays music on YouTube")
    @route.slash.describe(name_or_url="Enter title or url to search for YouTube music")
    async def play(self, interaction:Interaction, name_or_url:str):
        voice_client = interaction.guild.voice_client

        if not interaction.user.voice:
            await interaction.response.send_message("**You must be in a voice channel to use this command.**", ephemeral=True,delete_after=180)
            return
            
        if voice_client is None:
            await interaction.response.send_message("**The bot is not connected to the voice channel.**", ephemeral=True,delete_after=180)
            return

        await interaction.response.defer()
        
        yt_dlp_instance = YTDlp()
        search_results = yt_dlp_instance.search_or_url(name_or_url)

        self.queue_play_list.set(search_results)

        if not voice_client.is_playing():
            is_have_music = await self.play_next(interaction,False)
            if is_have_music == False:
                await interaction.followup.send("**Could not find the video on request.**", ephemeral=True)
                return

        await interaction.followup.send(embed=YTDlpEmbed.add_music_embed(search_results,interaction))


    @route.slash.command(name="next",description="Skipping music and play next music")
    async def next(self,interaction:Interaction):
        voice_client = interaction.guild.voice_client        
        if voice_client is None:
                await interaction.response.send_message("**The bot is not connected to the voice channel.**", ephemeral=True,delete_after=180)
                return
        
        if self.queue_play_list.len() == 0:
            await interaction.response.send_message(embed=YTDlpEmbed.empty_embed(interaction),ephemeral=True,delete_after=180)
            return
           
        
        next_music = self.queue_play_list.peek()
        self.is_repeat = False

        embed = YTDlpEmbed.next_music_embed(next_music,interaction)
        
        await interaction.response.send_message(embed=embed, ephemeral=True,delete_after=180)

        if voice_client.is_playing():
            voice_client.stop()

    async def play_next(self,interaction:Interaction,is_fetch = True) -> bool:
        url:str
        search_results:dict

        if self.queue_play_list.len() == 0 and self.is_repeat == False:
            return

        if self.is_repeat == False:
            result = self.queue_play_list.get()
            webpage_url = result["webpage_url"]

            if is_fetch:
                yt_dlp_instance = YTDlp()
                search_results = yt_dlp_instance.search_or_url(webpage_url)
            else:
                search_results = result

            if not search_results:
                return False

            self.now_play_info = search_results
            url = search_results["url"]
        else:
            url = self.now_play_info["url"]

        source = FFmpegOpusAudio(url, **self.FFMPEG_OPTIONS)
        interaction.guild.voice_client.play(source,after=lambda _: self.bot.loop.create_task(self.play_next(interaction)))
        return True
        

    @route.slash.command(name="stop",description="Stopping audio playback")
    async def stop(self, interaction:Interaction):
        voice_client = interaction.guild.voice_client

        if voice_client is None:
            await interaction.response.send_message("**The bot is not connected to the voice channel.**", ephemeral=True,delete_after=180)
            return
        
        self.queue_play_list.clear()
    
        voice_client.stop()
        await interaction.response.send_message("**Audio playback has stopped.**", ephemeral=True,delete_after=180)

    @route.slash.command(name="playlist",description="Adding a playlist to the queue")
    @route.slash.describe(playlist="Select playlist key")
    async def playlist(self,interaction: Interaction,playlist:str):
        voice_client = interaction.guild.voice_client
        
        if voice_client is None:
            await interaction.response.send_message("**The bot is not connected to the voice channel.**", ephemeral=True,delete_after=180)
            return

        playlist_manage = PlayList(playlist_key=playlist, dir=Dir.public)
        if not playlist_manage.is_playlist_exists:
            await interaction.response.send_message(f"**Your selected playlist not exists**\nYour selected playlist: **{playlist}**",ephemeral=True,delete_after=180)
            return
        
        selected_playlist = playlist_manage.selected_playlist

        if len(selected_playlist) == 0:
            await interaction.response.send_message("**Your playlist not have musics**",ephemeral=True,delete_after=180)
            return
        
        await interaction.response.defer()

        self.queue_play_list.extend(selected_playlist)
    
        if not voice_client.is_playing():
            await self.play_next(interaction)

        await interaction.followup.send("**Your playlist has been added queue**")

    @route.slash.command(name="show_queue",description="Show queue now playing musics")
    async def show_queue(self,interaction: Interaction):
        voice_client = interaction.guild.voice_client
        if voice_client is None:
            await interaction.response.send_message("**The bot is not connected to the voice channel.**", ephemeral=True,delete_after=180)
            return

        embed = YTDlpEmbed.get_embed(self.queue_play_list,interaction)
        await interaction.response.send_message(embed=embed,ephemeral=True,delete_after=180)


    @route.slash.command(name="pause", description="Pause your music")
    async def pause(self,interaction: Interaction):
        voice_client = interaction.guild.voice_client
        if voice_client is None:
            await interaction.response.send_message("**The bot is not connected to the voice channel.**", ephemeral=True,delete_after=180)
            return
        voice_client.pause()
        await interaction.response.send_message("**Your music has been paused**",ephemeral=True,delete_after=180)
    
    @route.slash.command(name="resume", description="Resume your music")
    async def resume(self,interaction: Interaction):
        voice_client = interaction.guild.voice_client
        if voice_client is None:
            await interaction.response.send_message("**The bot is not connected to the voice channel.**", ephemeral=True,delete_after=180)
            return
        voice_client.resume()
        await interaction.response.send_message("**Your music has been resume**",ephemeral=True,delete_after=180)

    @route.slash.command(name="now_play",description="View now playling music")
    async def now_play(self,interaction: Interaction):
        voice_client = interaction.guild.voice_client
        if voice_client is None:
            await interaction.response.send_message("**The bot is not connected to the voice channel**", ephemeral=True,delete_after=180)
            return
        if not voice_client.is_playing():
            await interaction.response.send_message("**Bot not playing music**",ephemeral=True,delete_after=180)
            return
        embed = YTDlpEmbed.now_music_play_embed(self.now_play_info,interaction)
        await interaction.response.send_message(embed=embed)

    @route.slash.command(name="repeat",description="Repeats currently playing music")
    async def repeat(self,interaction: Interaction):
        voice_client = interaction.guild.voice_client
        if not voice_client.is_playing():
            await interaction.response.send_message(f"**We cannot activate repeat because there is no music currently playing.**",ephemeral=True,delete_after=180)
            return
        
        self.is_repeat = not self.is_repeat
        answer = "Your played music will repeat" if self.is_repeat else "Your played music will not be repeated"
        await interaction.response.send_message(f"**{answer}**",ephemeral=True,delete_after=180)

async def setup(bot: Bot):
    await bot.add_cog(YTCog(bot))