from vkreborn.handlers.for_admins import giveadmin, takeadmin, invite_forceinvite_kick, mute

admin_labelers = {
    mute.labeler,
    giveadmin.labeler,
    takeadmin.labeler,
    invite_forceinvite_kick.labeler,
}

__all__ = ["admin_labelers"]
