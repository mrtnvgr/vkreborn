from vkreborn.handlers.for_admins import (
    giveadmin,
    takeadmin,
    invite_forceinvite_kick,
    mute,
    whreset,
)

admin_labelers = {
    mute.labeler,
    giveadmin.labeler,
    takeadmin.labeler,
    invite_forceinvite_kick.labeler,
    whreset.labeler,
}

__all__ = ["admin_labelers"]
