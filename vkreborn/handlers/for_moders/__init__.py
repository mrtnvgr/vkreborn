from vkreborn.handlers.for_moders import (
    forceinvite,
    givemoder,
    invite,
    kick,
    mute,
    takemoder,
    unmute,
    whreset,
)

moder_labelers = {
    mute.labeler,
    unmute.labeler,
    givemoder.labeler,
    takemoder.labeler,
    kick.labeler,
    invite.labeler,
    forceinvite.labeler,
    whreset.labeler,
}

__all__ = ["moder_labelers"]
