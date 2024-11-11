from discord import Interaction
from template.ui.select.select import Select

class UserSelect(Select):
    placeholder = "Выберете пользователя"
    options = {
        "Shayan": "User shayan"
    }
    async def handler(self, interaction: Interaction):
        await interaction.response.send_message(f"Вы выбрали: {interaction.data['values'][0]}")