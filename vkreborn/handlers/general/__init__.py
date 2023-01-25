from vkreborn.handlers.general import (
    new_user,
    muted,
    fixlayout,
    whoami,
    moders,
    roll,
    trans,
    shazam,
    wallhaven,
    helphandler,
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
    wallhaven.labeler,
    helphandler.labeler,
}

__all__ = ["general_labelers"]
