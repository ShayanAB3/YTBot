from template.ui.select.select import Select

from discord import Interaction

class SelectPlaylist(Select):
    placeholder = "Select the music you want to update"
    def handler(self, interaction:Interaction):
        return super().handler(interaction)