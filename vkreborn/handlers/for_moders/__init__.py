from vkreborn.handlers.for_moders import (
    givemoder,
    takemoder,
    invite_forceinvite_kick,
    mute,
    whreset,
)

moder_labelers = {
    mute.labeler,
    givemoder.labeler,
    takemoder.labeler,
    invite_forceinvite_kick.labeler,
    whreset.labeler,
}

__all__ = ["moder_labelers"]
