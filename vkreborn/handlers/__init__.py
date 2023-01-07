from vkreborn.handlers import (
    new_user,
    fixlayout,
    whoami,
    admins,
    roll,
    mute,
    giveadmin,
    takeadmin,
    trans,
)

labelers = {
    new_user.labeler,
    mute.labeler,
    giveadmin.labeler,
    takeadmin.labeler,
    fixlayout.labeler,
    whoami.labeler,
    admins.labeler,
    roll.labeler,
    trans.labeler,
}

__all__ = ["labelers"]
