from discord import Interaction
from template.ui.button.button import Button

class UserButton(Button):
    label = "Нажмите кнопку"

    async def handler(self, interaction: Interaction):
        await interaction.response.send_message("Кнопка нажата")