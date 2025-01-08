from discord.app_commands import Group as DiscordGroup
from discord.app_commands.translator import locale_str
from discord.utils import MISSING
from discord import Permissions
from discord.ext.commands import Bot, Cog

from typing import Union, Optional, Dict, Any

class Group(DiscordGroup):
    """
    Parameters

    name: Union[:class:`str`, :class:`locale_str`]
        The name of the group. If not given, it defaults to a lower-case
        kebab-case version of the class name.

    description: Union[:class:`str`, :class:`locale_str`]
        The description of the group. This shows up in the UI to describe
        the group. If not given, it defaults to the docstring of the
        class shortened to 100 characters.

    parent: Optional[:class:`Group`]
        The parent application command. ``None`` if there isn't one.

    guild_only: :class:`bool`
        Whether the command should only be usable in guild contexts.
        Due to a Discord limitation, this does not work on subcommands.

    nsfw: :class:`bool`
        Whether the command is NSFW and should only work in NSFW channels.
        Defaults to ``False``.
        Due to a Discord limitation, this does not work on subcommands.

    auto_locale_strings: :class:`bool`
        If this is set to ``True``, then all translatable strings will implicitly
        be wrapped into :class:`locale_str` rather than :class:`str`. This could
        avoid some repetition and be more ergonomic for certain defaults such
        as default command names, command descriptions, and parameter names.
        Defaults to ``True``.
    
    default_permissions: Optional[:class:`~discord.Permissions`]
        The default permissions that can execute this command on Discord. Note
        that server administrators can override this value in the client.
        Setting an empty permissions field will disallow anyone except server
        administrators from using the command in a guild.

    extras: :class:`dict`
        A dictionary that can be used to store extraneous data.
        The library will not touch any values or keys within this dictionary.
    """

    name: Union[str, locale_str]
    description: Union[str, locale_str]
    parent: Optional[DiscordGroup] = None
    guild_only: bool = MISSING
    nsfw: bool = False
    auto_locale_strings: bool = True
    default_permissions: Optional[Permissions] = MISSING,
    extras: Dict[Any, Any] = MISSING
    
    bot:Bot

    def __init__(self,bot:Bot):
        self.bot = bot
        super().__init__(name=self.name, description=self.description)
