from vkreborn.handlers import (
    new_user,
    fixlayout,
    whoami,
    admins,
    roll,
    mute,
    giveadmin,
    takeadmin,
    invite_forceinvite_kick,
    trans,
)

labelers = {
    new_user.labeler,
    mute.labeler,
    giveadmin.labeler,
    takeadmin.labeler,
    invite_forceinvite_kick.labeler,
    fixlayout.labeler,
    whoami.labeler,
    admins.labeler,
    roll.labeler,
    trans.labeler,
}

__all__ = ["labelers"]
