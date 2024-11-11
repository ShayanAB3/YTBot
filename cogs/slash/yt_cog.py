from cogs.cogs import Cogs
from discord import Interaction
from discord.ext.commands import Bot

from discord import FFmpegOpusAudio, Embed, Color

from route.route import route

from public.api.yt_dlp.yt_dlp import YTDlp

from facade.url.url import Url
from facade.structures_data.queue import Queue

class YTCog(Cogs):
    FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
    }
    queue_play_list = Queue()
    

    @route.slash.command(name="join", description="Joins a voice channel")
    async def join(self, interaction:Interaction):
        channel = interaction.user.voice.channel

        if not interaction.user.voice:
            await interaction.response.send_message("**You must be in a voice channel to use this command.**", ephemeral=True)
            return
        if interaction.guild.voice_client:
            await interaction.response.send_message(f"The bot is already connected to the channel **{channel.name}.**", ephemeral=True)
            return
        
        await channel.connect()
        await interaction.response.send_message(f"Joined voice channel: **{channel.name}**", ephemeral=True)
    

    @route.slash.command(name="leave", description="Leaves the voice channel")
    async def leave(self, interaction: Interaction):
        voice_client = interaction.guild.voice_client
        if not voice_client:
            await interaction.response.send_message("**The bot is not in the voice channel.**", ephemeral=True)

        await voice_client.disconnect()
        await interaction.response.send_message("**Left the voice channel.**", ephemeral=True)


    @route.slash.command(name="play",description="Plays music on YouTube")
    @route.slash.describe(name_or_url="Enter title or url to search for YouTube music")
    async def play(self, interaction:Interaction, name_or_url:str):
        voice_client = interaction.guild.voice_client
        
        if voice_client is None:
            await interaction.response.send_message("**The bot is not connected to the voice channel.**", ephemeral=True)
            return

        await interaction.response.defer()

        try:
            yt_dlp_instance = YTDlp()
            url = Url(name_or_url)
            search_results = yt_dlp_instance.url(name_or_url) if url.is_url() else yt_dlp_instance.search(name_or_url)
            if not search_results:
                await interaction.followup.send("**Could not find the video on request.**", ephemeral=True)
                return

            self.queue_play_list.set(search_results)

            if not voice_client.is_playing():
                await self.play_next(interaction)
                return
    
        except Exception as e:
            embed = Embed(title=e.__class__.__name__,
                          color=Color.red(),
                          description=e.__str__())
            await interaction.followup.send(embed=embed)



    @route.slash.command(name="next",description="Skipping music and play next music")
    async def next(self,interaction:Interaction):
        voice_client = interaction.guild.voice_client
        if voice_client is None:
                await interaction.response.send_message("**The bot is not connected to the voice channel.**", ephemeral=True)
                return
        
        await interaction.response.send_message("**Moving on to the next song**", ephemeral=True)

        if voice_client.is_playing():
            voice_client.stop()

    async def play_next(self,interaction:Interaction):
        len_before_queue_play_list = len(self.queue_play_list.quare)

        if self.queue_play_list.quare:
            info = self.queue_play_list.get()
            print("**Playing**")
            source = FFmpegOpusAudio(info["url"], **self.FFMPEG_OPTIONS)
            interaction.guild.voice_client.play(source,after=lambda _: self.bot.loop.create_task(self.play_next(interaction)))
        
        if len_before_queue_play_list != 1:
            await interaction.followup.send(embed=YTDlp.list_music_embed(self.queue_play_list.quare))
            return 

        await interaction.followup.send(embed=YTDlp.embed(info))
        

    @route.slash.command(name="stop",description="Stopping audio playback")
    async def stop(self, interaction:Interaction):
        voice_client = interaction.guild.voice_client

        if voice_client is None:
            await interaction.response.send_message("**The bot is not connected to the voice channel.**", ephemeral=True)
            return
        
        self.queue_play_list.clear()
        voice_client.stop()
        await interaction.response.send_message("**Audio playback has stopped.**", ephemeral=True)

async def setup(bot: Bot):
    await bot.add_cog(YTCog(bot))