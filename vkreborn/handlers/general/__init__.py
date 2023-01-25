from vkreborn.handlers.general import (
    fixlayout,
    helphandler,
    moders,
    muted,
    new_user,
    roll,
    shazam,
    tiktok,
    trans,
    wallhaven,
    whoami,
)
from vkreborn.handlers.general.fx import fx_labelers

general_labelers = {
    new_user.labeler,
    muted.labeler,
    *fx_labelers,
    fixlayout.labeler,
    whoami.labeler,
    moders.labeler,
    roll.labeler,
    trans.labeler,
    shazam.labeler,
    tiktok.labeler,
    wallhaven.labeler,
    helphandler.labeler,
}

__all__ = ["general_labelers"]
