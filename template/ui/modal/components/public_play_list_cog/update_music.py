from template.ui.modal.modal import Modal

from discord.ui import Modal as DiscordModal
from discord import Interaction

from public.playlists.playlist import PlayList, Dir

class UpdateMusic(Modal):
    title = "Update Music"
    
    async def on_submit(self, modal:DiscordModal, interaction: Interaction):
       name = modal.children[0].value
       age = modal.children[1].value
       await interaction.response.send_message(f"Имя: {name}, Возраст: {age}")