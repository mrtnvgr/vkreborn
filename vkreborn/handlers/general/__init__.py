from vkreborn.handlers.general import (
    demotivator,
    fixlayout,
    helphandler,
    moders,
    muted,
    muted_user,
    mutedby,
    new_user,
    roll,
    shazam,
    tiktok,
    trans,
    wallhaven,
    whoami,
    whois,
    whomuted,
)
from vkreborn.handlers.general.fx import fx_labelers

general_labelers = {
    new_user.labeler,
    muted_user.labeler,
    muted.labeler,
    mutedby.labeler,
    whomuted.labeler,
    demotivator.labeler,
    *fx_labelers,
    fixlayout.labeler,
    whoami.labeler,
    whois.labeler,
    moders.labeler,
    roll.labeler,
    trans.labeler,
    shazam.labeler,
    tiktok.labeler,
    wallhaven.labeler,
    helphandler.labeler,
}

__all__ = ["general_labelers"]
