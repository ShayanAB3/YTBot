from discord import Interaction
from discord.ui import TextInput, Modal as DiscordModal
from template.ui.modal.modal import Modal

class UserModal(Modal):
    title = "Ваша форма"
    items = [
        TextInput(label="Ваше имя", placeholder="Введите ваше имя..."),
        TextInput(label="Ваш возраст", placeholder="Введите ваш возраст...")
    ]
    
    async def on_submit(self, modal:DiscordModal, interaction: Interaction):
        name = modal.children[0].value
        age = modal.children[1].value
        await interaction.response.send_message(f"Имя: {name}, Возраст: {age}")