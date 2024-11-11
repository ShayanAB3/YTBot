from template.ui.button.button import Button
from discord import Interaction
from discord.enums import ButtonStyle

class MusicButton(Button):
    label = "Играть"
    style:ButtonStyle = 1
    
    def handler(self, interaction:Interaction):
        pass