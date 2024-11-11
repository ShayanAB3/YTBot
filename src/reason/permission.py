from src.reason.reason import Reason

class Permission(Reason):
    create_instant_invite: bool
    kick_members: bool
    ban_members: bool
    administrator: bool
    manage_channels: bool
    manage_guild: bool
    add_reactions: bool
    view_audit_log: bool
    priority_speaker: bool
    stream: bool
    read_messages: bool
    view_channel: bool
    send_messages: bool
    send_tts_messages: bool
    manage_messages: bool
    embed_links: bool
    attach_files: bool
    read_message_history: bool
    mention_everyone: bool
    use_external_emojis: bool
    view_guild_insights: bool
    connect: bool
    speak: bool
    mute_members: bool
    deafen_members: bool
    move_members: bool
    use_voice_activation: bool
    change_nickname: bool
    manage_nicknames: bool
    manage_roles: bool
    manage_webhooks: bool
    manage_emojis: bool
    use_slash_commands: bool
    request_to_speak: bool
    manage_threads: bool
    use_public_threads: bool
    use_private_threads: bool
    use_external_stickers: bool
    send_messages_in_threads: bool
    use_embedded_activities: bool
    moderate_members: bool

    def get(self) -> dict[str,bool]:
        return self.__dict__