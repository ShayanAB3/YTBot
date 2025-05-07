from discord import Embed, Color, Interaction
from facade.structures_data.queue import Queue

class YTDlpEmbed:

    def get_embed(queue:Queue,interaction: Interaction) -> Embed:
        len_before_queue_play_list = queue.len()
        is_playing = interaction.guild.voice_client.is_playing()

        if len_before_queue_play_list == 0:
            return YTDlpEmbed.empty_embed(interaction)
        
        if len_before_queue_play_list > 1 and is_playing:
            return YTDlpEmbed.list_music_embed(queue.queue)

        if len_before_queue_play_list == 1:
            return YTDlpEmbed.music_added_embed(queue.queue[0])

    def music_added_embed(info: dict[str]) -> Embed:
        embed = Embed(
            title=info.get("title"),
            description=info.get("channel"),
            color=Color.red(),
            url=info.get("webpage_url")
        )
        embed.set_author(name="YouTube", url=info.get("webpage_url"))
        embed.set_image(url=info.get("thumbnail"))
        return embed
    
    def empty_embed(interaction:Interaction) -> Embed:
        embed = Embed(
            title="**Queue is empty**",
            description="No songs are currently in the queue. Add some music to get started!",
            color=Color.red(),
        )
        embed.set_author(icon_url=interaction.user.avatar.url,name=f"{interaction.user.display_name}")
        return embed


    def next_music_embed(info: dict[str],interaction:Interaction) -> Embed:
        embed = Embed(
            title="Next song:",
            description=f"> ### [{info.get("title")}]({info.get("webpage_url")})\n> {info.get("channel")}",
            color=Color.red()
        )
        embed.set_author(icon_url=interaction.user.avatar.url,name=f"{interaction.user.display_name}")
        embed.set_image(url=info.get("thumbnail"))
        return embed

    def add_music_embed(info: dict[str], interaction: Interaction) -> Embed:
        embed = Embed(
            title="**​Music added to queue:**",
            description=f"\n> ### [{info.get("title")}]({info.get("webpage_url")})\n> {info.get("channel")}",
            color=Color.red()
        )
        embed.set_author(icon_url=interaction.user.avatar.url,name=f"{interaction.user.display_name}")
        embed.set_image(url=info.get("thumbnail"))
        return embed

    def list_music_embed(data:list[dict[str]])-> Embed:
        embed = Embed(
        title="**List musics:**",
        description=f"**Count music: ** `{len(data)}`\nList music: ",
        color=Color.red(),
        )
        for i, info in enumerate(data):
            if i >= 25:
                break
            embed.add_field(name=info["title"], value=f"{info["channel"]}",inline=False)
        return embed
    
    def now_music_play_embed(info: dict[str],interaction: Interaction) -> Embed:
        embed = Embed(title="**Now play:**",
                      description=f"\n> ### [{info.get("title")}]({info.get("webpage_url")})\n> {info.get("channel")}",
                      color=Color.red())
        embed.set_author(icon_url=interaction.user.avatar.url,name=f"{interaction.user.display_name}")
        embed.set_image(url=info.get("thumbnail"))
        return embed